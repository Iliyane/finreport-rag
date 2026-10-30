from __future__ import annotations

import os
from pathlib import Path


def ensure_directories() -> None:
    directories = [
        Path("./data/documents"),
        Path("./data/vectorstore"),
        Path("./data/output"),
    ]
    for folder in directories:
        folder.mkdir(parents=True, exist_ok=True)


def list_pdf_files(folder: str) -> list[str]:
    target = Path(folder)
    if not target.exists():
        return []
    return sorted(str(path) for path in target.iterdir() if path.suffix.lower() == ".pdf")
