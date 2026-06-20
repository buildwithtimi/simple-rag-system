# Simple RAG system

A lightweight, simple Retrieval-Augmented Generation (RAG) system built from scratch in Python. This system ingests the official *Pro Git* book chapters, indexes it into a local vector database, and uses semantic search combined with Google's Gemini API to answer technical Git questions with absolute factual accuracy.

[attachment_0](attachment)

---

## 🛠️ System Architecture

The application is engineered using clean architecture principles, strictly isolating the data, storage, and generation layers:

1. **Ingestion Layer (`src/ingest.py`)**: Recursively walks through nested book directories using `pathlib` to extract text from 112 Asciidoc (`.asc`) files. It utilizes a `RecursiveCharacterTextSplitter` to generate 1,313 contextual fragments (800 characters, 100-character overlap) without slicing code or commands mid-line.
2. **Storage Layer (`src/database.py`)**: Initializes a persistent local **ChromaDB** instance. Chunks are automatically vectorized using local embeddings and stored safely on disk alongside structural metadata for strict provenance tracking.
3. **Retrieval Pipeline**: Executes mathematical similarity searches against the persistent vector space to surface the top $K$ most relevant text blocks matching a user's natural language query.
4. **Generation Layer (`src/generator.py`)**: Wraps the query and retrieved text in a highly constrained system prompt. It leverages `gemini-2.5-flash` with zero temperature to eliminate AI hallucinations and ensure answers are grounded strictly in the book's text.

---

## 📂 Repository Structure

```text
simple-git-rag/
├── data/
│   └── pro-git-book/       # Raw Pro Git .asc text corpus
├── chroma_db/              # Generated persistent vector store binaries
├── src/
│   ├── __init__.py
│   ├── ingest.py           # Corpus parsing & recursive chunking logic
│   ├── database.py         # ChromaDB interface (seeding & querying)
│   ├── generator.py        # Gemini API integration & prompt isolation
│   └── main.py             # App orchestrator & interactive CLI loop
├── .env                    # Local credentials (git-ignored)
├── .gitignore              # Security and artifact filters
└── pyproject.toml          # Project metadata and uv dependencies
```

---

## 🚀 Getting Started

​Prerequisites
​This project utilizes uv, the ultra-fast Python package and project manager. If you do not have it installed, run the following command in your terminal:

    # Windows (PowerShell)
    irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex

Installation & Setup
1. ​Clone the repository and navigate to the project root:

    git clone <your-repo-url>
    cd simple-git-rag

2. ​Configure your environment variables:
   Create a file named .env in the root directory and paste your Google AI Studio credential inside:

3. ​Install dependencies automatically:
   The project dependencies are managed via uv. They will automatically install the first time you run the application.

---

## 💻 Usage

​To launch the interactive command-line interface loop, execute the application as a module from the root directory:

    uv run python -m src.main

Example Queries to Try:
1. ​How do I undo a commit that hasn't been pushed yet?
2. ​What is the difference between git reset and git revert?
3. ​How do I configure my username and email for the first time?