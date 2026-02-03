# Sanskrit Document Retrieval-Augmented Generation (RAG) System

This project implements an end-to-end Retrieval-Augmented Generation (RAG) pipeline for Sanskrit documents. It ingests Sanskrit .txt files, builds a FAISS vector index, retrieves relevant context, and generates answers using a CPU-based LLM.

## Folder Structure

```
immverse_ai_rag_project/
├── code/
│   ├── build_index.py
│   ├── ingest.py
│   ├── pipeline.py
│   ├── preprocess.py
│   ├── query.py
│   ├── requirements.txt
│   └── faiss_index/ # Created after running build_index.py
|          
├── data/
│   ├── murkhabhritya.txt
│   ├── devbhakt.txt
│   ├── ghantakarna.txt
│   ├── kalidas.txt
│   └── sheetam.txt
├── report/
│   ├── report.pdf
│   └── report.md
└── README.md
```

## Features

- ✅ CPU-only inference (No GPU required)
- ✅ Sanskrit document ingestion (.txt)
- ✅ Preprocessing + chunking
- ✅ Semantic retrieval using FAISS vector store
- ✅ Answer generation using CPU-based LLM (google/flan-t5-small)
- ✅ Interactive query interface (Terminal / CLI)

## Tech Stack

- Python 3.10+
- LangChain
- FAISS
- SentenceTransformers
- HuggingFace Transformers
- LLM Model: google/flan-t5-small (CPU-friendly)

## Setup Instructions (VS Code + Terminal)

### 1) Create Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 2) Install Dependencies

```bash
pip install -r code/requirements.txt
```

## Execution Steps

### Step 1: Build Vector Index (Ingestion)

This loads documents from `/data`, splits them into chunks, generates embeddings, and builds a FAISS vector index.

```bash
python code/build_index.py
```

Expected Output:
```
📥 Loading Sanskrit documents from /data ...
✅ Loaded documents: 5
✂️ Splitting into chunks...
✅ Total chunks: XX
🧠 Creating embeddings...
📦 Building FAISS index...
✅ Saved index to: code/faiss_index
```

### Step 2: Run Query Interface (RAG QA System)

```bash
python code/query.py
```

Expected Output:

```

======================================================================     
✅ Sanskrit Document Retrieval-Augmented Generation System
✅ CPU-only Inference Enabled
======================================================================     

Enter Sanskrit Query (or type 'exit'):
```


