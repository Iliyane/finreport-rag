from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from app.config import settings

app = FastAPI(
    title="Finance Report RAG",
    description="Advanced RAG for financial reports, balance sheets, performance data, and prospectuses.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.app_env,
    }


@app.post("/api/query")
def handle_query(payload: dict):
    question = payload.get("question", "").strip()

    if not question:
        raise HTTPException(status_code=400, detail="A valid question is required.")

    response = {
        "answer": "This is the starter response. Connect the retrieval and validation layers to answer real financial questions from your documents.",
        "question": question,
        "sources": [
            {
                "document": "example-report.pdf",
                "page": 18,
                "table": "Table 5",
                "snippet": "Placeholder citation for finance-grounded responses."
            }
        ],
        "confidence": "medium",
    }

    return response
