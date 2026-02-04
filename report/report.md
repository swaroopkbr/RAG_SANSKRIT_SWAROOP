✅ Technical Report
Sanskrit Document Retrieval-Augmented Generation (RAG) System (CPU Based)
Project Title:

Sanskrit Document Retrieval-Augmented Generation (RAG) System

Submitted By:

Swaroop Kumbhalwar

Project Folder Name:

immverse_ai_rag_project

1. Objective

The main aim of this project is to build a Retrieval-Augmented Generation (RAG) system that can answer questions using a collection of Sanskrit documents.
A key requirement of the assignment is that the complete pipeline should run only on CPU-based inference, without using any GPU resources.

This ensures the solution remains lightweight, efficient, and deployable on basic hardware.

2. Project Overview

This project is an end-to-end implementation of a Sanskrit-aware RAG pipeline.
The system is designed to:

Load Sanskrit documents stored in plain text format

Clean and split the content into smaller meaningful chunks

Create embeddings and index the chunks for fast retrieval

Accept Sanskrit user queries at runtime

Retrieve the most relevant document chunks from the corpus

Generate accurate answers using a lightweight CPU-supported LLM

The overall structure follows standard modular RAG principles, where retrieval and generation are clearly separated.

3. System Architecture and Workflow
3.1 Overall RAG Execution Flow

The pipeline follows the below stages:

Document Loading

Text Cleaning and Chunking

Semantic Embedding Creation

Vector Index Construction using FAISS

User Query Input via CLI

Retrieval of Top-k Relevant Chunks

Prompt Formation with Retrieved Context

Answer Generation using LLM

Final Output with Supporting Sources

3.2 Module-Based Architecture

The system is divided into two primary modules:

A. Indexing Pipeline (Offline Stage)

File: build_index.py

This module prepares the retrieval system in advance:

Sanskrit text files are loaded from the /data folder

Documents are split into context chunks

Embeddings are generated for each chunk

A FAISS vector index is created and stored inside /code/faiss_index

This indexing step is executed once before querying.

B. Query Pipeline (Online Stage)

File: query.py

This module handles real-time question answering:

Loads the stored FAISS index from disk

Performs similarity-based retrieval using MMR

Passes relevant context + query into the LLM

Displays the generated answer along with supporting evidence

4. Sanskrit Document Dataset

The document corpus contains Sanskrit stories and subhashitas stored as individual .txt files under /data/.

Each document is separated story-wise to ensure better retrieval grounding and prevent topic mixing.

Files Included:

murkhabhritya.txt – मूर्खभृत्यस्य (Shankhnad story)

devbhakta.txt – देवभक्तः कथा (faith and effort)

ghantakarna.txt – वृद्धायाः चातुर्यम् / घण्टाकर्णः कथा

kalidasa.txt – चतुरस्य कालीदासस्य कथा

sheetam.txt – शीतं बहु बाधति कथा

Maintaining separate files significantly improves answer relevance during retrieval.

5. Text Preprocessing Pipeline
5.1 Document Loading

Documents are loaded through:

DirectoryLoader

TextLoader(encoding="utf-8")

UTF-8 encoding ensures proper handling of Devanagari text.

5.2 Chunk Creation

Since long documents cannot be passed directly into an LLM, the text is split using:

RecursiveCharacterTextSplitter

Chunk configuration:

chunk_size = 350

chunk_overlap = 50

This helps in:

Improving retrieval precision

Avoiding context overflow

Retaining continuity between chunks

5.3 Embedding Generation

To represent Sanskrit chunks semantically, embeddings are created using:

sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

Chosen because it is:

Efficient for CPU usage

Supports multilingual semantic similarity

Works effectively for Sanskrit-like scripts

6. Retrieval System
6.1 Vector Storage

The retrieval layer is powered by:

✅ FAISS (CPU Vector Store)

FAISS enables fast similarity search and local indexing without GPU dependency.

6.2 Retrieval Technique

The retriever uses:

✅ MMR (Max Marginal Relevance)

This strategy improves retrieval by:

Selecting relevant but diverse chunks

Reducing repetitive context

Enhancing grounding for generation

7. Answer Generation Component
7.1 CPU-Compatible LLM

The generation model used is:

google/flan-t5-small

This model was selected because:

It is lightweight and fast on CPU

Works well for QA tasks

Requires significantly less memory

7.2 Prompt Engineering

A strict prompt format is used to ensure:

Answers are only based on retrieved context

Hallucinations are minimized

If the context does not contain an answer, the system responds with:

"सन्दर्भे उत्तरं न लभ्यते।"

Additionally, retrieved sources are printed for transparency.

8. Performance Observations
8.1 Latency

Retrieval using FAISS is extremely fast (generally < 1 second)

LLM generation speed depends on CPU power, usually taking a few seconds

8.2 Resource Efficiency

The complete system runs without GPU support.
Main resource consumption comes from:

Embedding model memory

FAISS index size

FLAN-T5 inference load

Using flan-t5-small keeps RAM usage low and inference efficient.

8.3 Answer Quality and Relevance

System accuracy depends heavily on retrieval quality.

Key improvements noticed:

Story-wise separation reduces incorrect context overlap

MMR selects better diverse chunks

Example:

Query: शंखनादः कः?

Correctly retrieved from murkhabhritya.txt

Generated Answer:

शंखनादः गोवर्धनदासस्य भृत्यः (आज्ञापालकः) अस्ति।

9. Conclusion

The Sanskrit Document Retrieval-Augmented Generation (RAG) System was successfully developed as a complete CPU-only question answering pipeline.

The system:

Ingests Sanskrit texts

Chunks and embeds content

Indexes using FAISS

Retrieves relevant context

Generates grounded answers using FLAN-T5

This implementation satisfies all assignment requirements while following a clean modular RAG architecture.

10. Future Enhancements

Possible improvements include:

Sanskrit transliteration support (English → Devanagari conversion)

PDF ingestion support using PyPDFLoader

Sanskrit-specialized embedding models for better accuracy

Building a UI demo using Streamlit or Flask

Adding evaluation metrics like retrieval precision and relevance scoring
