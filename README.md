# Finance Report RAG

Finance Report RAG is an Advanced RAG system built for analyzing long and complex financial documents such as annual reports, balance sheets, management reports, performance summaries, and fund prospectuses. The system is designed to extract relevant information from financial documents and answer quantitative questions with source-grounded evidence.

## Project goal

The goal of this project is to support questions such as:
- What was the net income in 2024?
- How did operating margin evolve over the last three years?
- Which fund had the strongest risk-adjusted return?
- What was the expense ratio in the latest prospectus?

These questions require more than keyword search. They demand structured table understanding, metadata-aware retrieval, and evidence validation.

## Why this project matters

Financial documents are dense and highly structured. Important facts often live in tables, footnotes, disclosures, and performance sections rather than in plain narrative text. A practical financial RAG system must therefore:
- read documents at the page and table level
- understand tabular structure
- normalize financial values and units
- retrieve the right evidence before answering
- validate the final answer against source content

## Architecture

The system follows a modular pipeline:

1. Document ingestion
   - read PDFs and other supported financial files
   - extract page images

2. Table detection
   - identify table regions in the page images
   - crop the relevant table areas

3. Multimodal extraction
   - pass table images to a multimodal model
   - extract values, captions, and relationship context

4. Retrieval and grounding
   - index relevant sections and tables
   - retrieve the strongest evidence for the question

5. Answer generation
   - produce an answer with citations to document, page, and table
   - provide a confidence indication and source context

## Repository structure

```text
.
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   └── services/
│       ├── __init__.py
│       ├── pdf_to_images.py
│       ├── table_detector.py
│       └── finance_rag.py
├── scripts/
│   └── finance_table_rag.py
├── data/
│   └── README.md
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
├── main.py
└── .env
```

## Tech stack

- Python
- FastAPI
- PyMuPDF
- Pillow
- Torch and Torchvision
- Transformers
- LlamaIndex
- OpenAI multimodal models
- FAISS or Qdrant for vector storage
- optional OCR tools such as EasyOCR

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/Iliyane/finreport-rag.git
cd finreport-rag
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the environment

```bash
cp .env.example .env
```

Then add your credentials in `.env`.

### 5. Run the API

```bash
uvicorn app.main:app --reload
```

### 6. Run the document analysis script

```bash
python main.py
```

## Secure configuration

This project requires environment variables for credentials. Do not commit secrets directly into source files.

Example `.env`:

```env
OPENAI_API_KEY=your_openai_key_here
HF_TOKEN=your_huggingface_token_here
```

## Security recommendations

- keep `.env` out of Git tracking
- use a secret manager in production
- avoid logging financial documents with private data in shared systems
- never store personal or regulated financial information in public repositories

## MVP roadmap

### Completed starter version
- project scaffold
- English documentation
- FastAPI starter API
- modular PDF conversion service
- table detection service
- multimodal finance query entry point

### Production roadmap
- document indexing with vector database
- table-aware retrieval and reranking
- answer verification against original document sources
- multi-document comparison support
- enterprise authentication and logging

## License

MIT

## Project status

This repository is a funded starter for a finance-focused multimodal RAG application. It is ready to be extended with real document ingestion, retrieval, and source-grounded answer generation for financial documents.
