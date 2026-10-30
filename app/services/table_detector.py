from __future__ import annotations

import os
from pathlib import Path

import torch
from PIL import Image


class MaxResize:
    def __init__(self, max_size: int = 800):
        self.max_size = max_size

    def __call__(self, image):
        width, height = image.size
        max_dim = max(width, height)
        scale = self.max_size / max_dim
        return image.resize((int(round(scale * width)), int(round(scale * height))))


def build_detection_transform():
    try:
        from torchvision import transforms
    except ImportError as exc:
        raise ImportError("torchvision is required for table detection.") from exc

    return transforms.Compose([
        MaxResize(800),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])


def box_cxcywh_to_xyxy(x):
    x_c, y_c, w, h = x.unbind(-1)
    b = [
        (x_c - 0.5 * w),
        (y_c - 0.5 * h),
        (x_c + 0.5 * w),
        (y_c + 0.5 * h),
    ]
    return torch.stack(b, dim=1)


def rescale_bboxes(out_bbox, size):
    width, height = size
    boxes = box_cxcywh_to_xyxy(out_bbox)
    boxes = boxes * torch.tensor([width, height, width, height], dtype=torch.float32)
    return boxes


def outputs_to_objects(outputs, img_size, id2label):
    logits = outputs.logits.softmax(-1)
    max_scores = logits.max(-1)
    pred_labels = list(max_scores.indices.detach().cpu().numpy())[0]
    pred_scores = list(max_scores.values.detach().cpu().numpy())[0]
    pred_bboxes = outputs["pred_boxes"].detach().cpu()[0]
    pred_bboxes = [elem.tolist() for elem in rescale_bboxes(pred_bboxes, img_size)]

    objects = []
    for label, score, bbox in zip(pred_labels, pred_scores, pred_bboxes):
        class_label = id2label[int(label)]
        if class_label != "no object":
            objects.append({
                "label": class_label,
                "score": float(score),
                "bbox": [float(elem) for elem in bbox],
            })
    return objects


def detect_and_crop_tables(image_path: str, output_dir: str, model, detection_transform) -> list[str]:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    image = Image.open(image_path)
    filename = Path(image_path).stem
    device = "cuda" if torch.cuda.is_available() else "cpu"

    pixel_values = detection_transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(pixel_values)

    id2label = model.config.id2label.copy()
    id2label[len(model.config.id2label)] = "no object"

    detected_tables = outputs_to_objects(outputs, image.size, id2label)
    created_files: list[str] = []

    for idx, table in enumerate(detected_tables):
        x1, y1, x2, y2 = [int(v) for v in table["bbox"]]
        cropped = image.crop((x1, y1, x2, y2))
        target_path = os.path.join(output_dir, f"{filename}_table_{idx + 1}.png")
        cropped.save(target_path)
        created_files.append(target_path)

    return created_files
