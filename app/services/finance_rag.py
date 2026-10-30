from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


class FinanceRAG:
    def __init__(self, vector_store=None, llm_client=None):
        self.vector_store = vector_store
        self.llm_client = llm_client

    def answer_question(self, question: str) -> Dict[str, Any]:
        return {
            "question": question,
            "answer": "The system is ready for implementation. Connect retrieval and validation layers to generate grounded answers.",
            "sources": [
                {
                    "document": "pending",
                    "page": None,
                    "section": "pending",
                    "table": None,
                    "confidence": "pending",
                }
            ],
            "metrics": [],
            "calculation": "No calculation performed yet.",
        }

    def build_query_plan(self, question: str) -> List[str]:
        return [
            "Identify the relevant report type",
            "Locate relevant sections and tables",
            "Extract financial metrics",
            "Validate the numeric answer against source documents",
        ]


def extract_document_metadata(file_path: str) -> Dict[str, Any]:
    path = Path(file_path)
    return {
        "filename": path.name,
        "extension": path.suffix.lower(),
        "size_bytes": path.stat().st_size if path.exists() else 0,
        "document_type": "financial-report",
        "status": "metadata_extracted",
    }
