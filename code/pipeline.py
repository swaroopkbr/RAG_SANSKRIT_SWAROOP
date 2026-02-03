import faiss
import numpy as np
import pickle
import os

from sentence_transformers import SentenceTransformer
from transformers import pipeline

# project root folder
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# paths to save index and chunks file
INDEX_PATH = os.path.join(PROJECT_ROOT, "faiss_index.idx")
CHUNKS_PATH = os.path.join(PROJECT_ROOT, "chunks.pkl")

# retriever embedding model
embedder = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# generator model (CPU-only)
generator = pipeline(
    "text-generation",
    model="gpt2",
    device=-1
)


def retrieve_context(query, top_k=3):
    """ Retrieves top Sanskrit chunks from FAISS index. """

    index = faiss.read_index(INDEX_PATH)

    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)

    query_embedding = embedder.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    return [chunks[i] for i in indices[0]]


def generate_answer(query):
    """ Generates final grounded answer using retrieved context."""

    retrieved_chunks = retrieve_context(query)

    if len(retrieved_chunks) == 0:
        return [], "उत्तरं न उपलब्धम्।"

    context = "\n".join(retrieved_chunks)

    prompt = f"""Answer the following question based on the context provided.

Context:
{context}

Question: {query}

Answer:"""

    output = generator(prompt, max_length=150, num_return_sequences=1)

    return retrieved_chunks, output[0]["generated_text"]
