# Finance Report RAG

Finance Report RAG is an advanced document intelligence system for analyzing long and complex financial documents such as annual reports, balance sheets, performance reports, and fund prospectuses. The system is designed to extract relevant tables, reason over the financial content, and answer quantitative questions with source-grounded evidence.

## Why this project exists

Financial documents rarely present the important information in continuous prose alone. Most critical insights live in tables, footnotes, performance summaries, and structured disclosures. A conventional RAG system that only searches raw text is often insufficient for financial analysis.

This project combines:
- PDF ingestion and page extraction
- table detection and cropping
- multimodal reasoning over document images
- source-aware retrieval and answer generation
- financial question handling for quantitative and comparative queries

## Core capabilities

- convert PDFs into page images
- detect and crop tables from report pages
- pass table images to a multimodal LLM for extraction and reasoning
- answer questions grounded in the original report content
- support multi-document comparison and document-level evidence retrieval

## Example questions

- What was the net income in 2024?
- How did operating margin change over the last three years?
- Which fund had the highest risk-adjusted return?
- What was the expense ratio in the latest prospectus?

## Architecture

The project follows a modular finance-document pipeline:

1. Ingestion
   - load PDF files from a local folder or upload interface
   - split pages into images

2. Table detection
   - detect table regions using a vision model
   - crop each detected table into a dedicated image

3. Extraction and reasoning
   - pass relevant table images to GPT-4o or another multimodal model
   - ask domain-specific questions grounded in those table images

4. RAG / evidence layer
   - index the extracted tables and supporting text
   - retrieve the strongest evidence before answering

5. Answer validation
   - verify that any metric or value comes from a valid source table or text section

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
├── README.md
├── requirements.txt
├── main.py
└── Dockerfile
```

## Tech stack

- Python
- FastAPI
- PyMuPDF
- Pillow
- Transformers
- Torch and Torchvision
- LlamaIndex
- OpenAI multimodal models
- Qdrant or FAISS for vector storage
- optional OCR support with EasyOCR

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

### 4. Configure environment variables

```bash
cp .env.example .env
```

Then add your secrets to `.env`.

## Secure configuration

Do not hardcode credentials directly in the source code.
Use environment variables instead.

Example:

```env
OPENAI_API_KEY=your_key_here
HF_TOKEN=your_hf_token_here
```

## Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:
- http://localhost:8000
- http://localhost:8000/docs

## Run the table-aware analysis script

```bash
python main.py
```

This script will:
- convert the PDF into images
- detect tables
- crop extracted tables
- prepare the data for multimodal analysis

## Security guidance

- never commit API keys or token values
- keep `.env` out of version control
- use a secure secret manager in production
- avoid logging sensitive document content in shared environments

## Recommended next steps

### MVP roadmap
- PDF ingestion for local documents
- table detection and cropping
- multimodal Q&A on extracted table images
- source-grounded answer structure

### Production roadmap
- vector database integration
- metadata indexing by company, year, and report type
- answer verification layer
- multi-document comparison workflows
- secure API and user authentication

## License

MIT

## Project status

This repository is a strong foundation for a finance-specific multimodal RAG pipeline and is designed to be extended into a production-grade document intelligence system.
