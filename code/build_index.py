import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

from ingest import load_documents
from preprocess import chunk_documents


MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def build_faiss_index():
    
    """Sanskrit Docs → Chunking → Embeddings → FAISS Index"""

    print("\n📌 Loading Documents...")
    documents = load_documents()

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

    # Save index
    faiss.write_index(index, "faiss_index.idx")

    # Save chunks
    with open("chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("\n✅ Index Built Successfully!")
    print("✅ Total Chunks:", len(chunks))


if __name__ == "__main__":
    build_faiss_index()
