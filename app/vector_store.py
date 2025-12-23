# import necessary libraries
import json
import os
import chromadb
from sentence_transformers import SentenceTransformer

# Define paths and constants
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PERSIST_DIR = os.path.join(BASE_DIR, "chroma_db")
COLLECTION_NAME = "trivia_chunks"

# Function to store embeddings in ChromaDB
def store_embeddings():
    with open("data/trivia_chunks.json", "r", encoding="utf-8") as f:
        chunks = json.load(f)

    texts = [item["text"] for item in chunks]
    ids = [str(item["id"]) for item in chunks]
    metadatas = [{"question": item["question"]} for item in chunks]

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts, batch_size=32, show_progress_bar=True)

    # Initialize ChromaDB client and collection
    client = chromadb.PersistentClient(path=PERSIST_DIR)

    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    collection.add(
        documents=texts,
        embeddings=embeddings.tolist(),
        metadatas=metadatas,
        ids=ids
    )

    print(f"Stored {len(texts)} embeddings in ChromaDB")


if __name__ == "__main__":
    store_embeddings()
