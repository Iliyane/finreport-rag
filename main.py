from __future__ import annotations

import os

from transformers import AutoConfig, AutoModelForObjectDetection

from app.services.pdf_to_images import pdf_to_images
from app.services.table_detector import detect_and_crop_tables, build_multimodal_llm
from app.services.table_detector import query_table_images
from app.services.table_detector import build_multimodal_llm as build_llm
from app.services.table_detector import query_table_images as ask_tables
from app.services.table_detector import build_multimodal_llm
from app.services.table_detector import query_table_images
from app.services.pdf_to_images import pdf_to_images
from app.services.table_detector import build_detection_transform


def main():
    pdf_file = "Investment_Fund.pdf"
    image_dir = "./pdf_images"
    table_dir = "./table_images"

    if not os.path.exists(pdf_file):
        raise FileNotFoundError(f"PDF not found: {pdf_file}")

    pdf_to_images(pdf_file, image_dir)

    model_id = "microsoft/table-transformer-structure-recognition"
    config = AutoConfig.from_pretrained(model_id)
    if hasattr(config, "dilation") and config.dilation is None:
        config.dilation = False

    model = AutoModelForObjectDetection.from_pretrained(model_id, config=config)
    detection_transform = build_detection_transform()

    image_files = sorted([
        os.path.join(image_dir, p)
        for p in os.listdir(image_dir)
        if p.lower().endswith(".png")
    ])

    for image_file in image_files:
        detect_and_crop_tables(image_file, table_dir, model, detection_transform)

    if os.path.exists(table_dir) and os.listdir(table_dir):
        prompt = (
            "Summarize the relevant financial content in the detected tables and identify "
            "the main table or section that answers the document question."
        )
        response = ask_tables(table_dir, prompt)
        print(response)


if __name__ == "__main__":
    main()
