from __future__ import annotations

import os
from pathlib import Path


def ensure_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)


def pdf_to_images(pdf_file: str, output_dir: str) -> list[str]:
    ensure_dir(output_dir)

    import fitz
    from PIL import Image

    pdf_document = fitz.open(pdf_file)
    generated_files: list[str] = []

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        image_path = os.path.join(output_dir, f"page_{page_number + 1}.png")
        image.save(image_path)
        generated_files.append(image_path)

    pdf_document.close()
    return generated_files
