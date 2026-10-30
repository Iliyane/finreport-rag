from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


def extract_document_metadata(file_path: str) -> Dict[str, Any]:
    path = Path(file_path)
    return {
        "filename": path.name,
        "extension": path.suffix.lower(),
        "size_bytes": path.stat().st_size if path.exists() else 0,
        "document_type": "financial-report",
        "status": "metadata_extracted",
    }


def extract_tables_from_pdf(file_path: str) -> List[Dict[str, Any]]:
    if not Path(file_path).exists():
        return []

    return [
        {
            "source_file": file_path,
            "page": 1,
            "table_id": "table_1",
            "caption": "Placeholder table",
            "headers": ["Metric", "Value"],
            "rows": [],
        }
    ]
