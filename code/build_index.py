import faiss
import numpy as np
import pickle
import os
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
from preprocess import chunk_documents

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

def load_documents(data_folder="data"):
    """Loads all the Sanskrit documents from txt and pdf files and return the list of raw text."""
    documents = []
    # Adjust path to be relative to project root if running from root, or relative to script if running from code/
    # The user runs python code/ingest.py, so data is likely ../data or just data if cwd is root?
    # User instruction says runs from root: python code/ingest.py
    # So data folder is just "data" if strictly following structure
    
    if not os.path.exists(data_folder):
         # Try looking one level up just in case
        if os.path.exists(os.path.join("..", data_folder)):
            data_folder = os.path.join("..", data_folder)
    
    if not os.path.exists(data_folder):
        print(f"Warning: Data folder '{data_folder}' not found.")
        return []

    for file_name in os.listdir(data_folder):
        file_path = os.path.join(data_folder, file_name)

        # Load TXT file
        if file_name.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                documents.append(f.read())

        # Load PDF file
        elif file_name.endswith(".pdf"):
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            documents.append(text)

    return documents

def build_faiss_index():
    """Sanskrit Docs → Chunking → Embeddings → FAISS Index"""

    print("\n📌 Loading Documents...")
    documents = load_documents()

    if not documents:
        print("❌ No documents found. Exiting.")
        return

    print(f"✅ Loaded documents: {len(documents)}")

    print("📌 Chunking Sanskrit Text...")
    chunks = chunk_documents(documents)

    print("📌 Loading Embedding Model (CPU)...")
    embedder = SentenceTransformer(MODEL_NAME)

    print("📌 Creating Chunk Embeddings...")
    embeddings = embedder.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")

    print("📌 Building FAISS Vector Index...")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    # Save index - path should be relative to code/ or where script is run?
    # User structure: code/faiss_index (folder) or just file?
    # User README says: "Saved index to: code/faiss_index" and structure shows code/faiss_index/
    # But code says faiss.write_index(index, "faiss_index.idx")
    # I will adapt to use a folder if that is what they want, but faiss usually saves a file.
    # The user structure shows `code/faiss_index/` as a folder # Created after running ingest.py
    # So I should probably save it into that folder.
    
    output_dir = "code/faiss_index"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        
    index_path = os.path.join(output_dir, "index.faiss")
    chunks_path = os.path.join(output_dir, "chunks.pkl")

    faiss.write_index(index, index_path)

    # Save chunks
    with open(chunks_path, "wb") as f:
        pickle.dump(chunks, f)

    print(f"✅ Saved index to: {output_dir}")
    print(f"✅ Total Chunks: {len(chunks)}")


if __name__ == "__main__":
    build_faiss_index()
