# README.md

# Finance Report RAG

This repository is a professional starter project for an Advanced RAG system focused on financial documents. It is designed to work with annual reports, balance sheets, performance reports, fund prospectuses, and other dense financial source materials.

## What this project does

The system aims to answer complex financial questions with evidence-backed results instead of generic document summaries. Examples include:
- "What was the net equity in 2024?"
- "How did the operating margin change over the last three years?"
- "Which fund had the best risk-adjusted return?"
- "What was the expense ratio in the latest prospectus?"

These questions require table-aware extraction, document-level reasoning, and numerical validation before a final answer is returned.

## Why this matters

Financial documents often contain the most important information in tables and structured sections. A simple search system cannot reliably answer questions like these unless it understands the document structure and validates the numerical evidence.

## Project architecture

The project combines:
- document ingestion
- PDF parsing and OCR
- table extraction and normalization
- hybrid retrieval
- grounded answer generation
- source validation for financial numbers

## Software stack

- Python
- FastAPI
- LlamaIndex or LangChain
- FAISS or Qdrant
- PyMuPDF and table extraction tools
- pandas
- OpenAI or Azure OpenAI

## Repository structure

```text
.
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   └── services/
│       ├── __init__.py
│       ├── document_processor.py
│       └── finance_rag.py
├── scripts/
│   └── finance_table_rag.py
├── data/
│   └── README.md
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── Dockerfile
```

## Quick start

```bash
git clone https://github.com/Iliyane/finreport-rag.git
cd finreport-rag
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Security

Do not hardcode API keys, tokens, or secrets in source files. Keep them in `.env` and load them from environment variables.

## Next steps

This repository is intended as the foundation for a realistic finance-focused RAG application. The next stage is to connect it to real document ingestion, a vector store, and a grounded answer pipeline.
