##import necessary libraries
import json
from sentence_transformers import SentenceTransformer

INPUT_PATH = "data/trivia_chunks.json"

##function to create embeddings
def create_embeddings():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    model = SentenceTransformer("all-MiniLM-L6-v2")

    texts = [item["text"] for item in chunks]

    embeddings = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=True
    )

    print(f"Generated embeddings shape: {embeddings.shape}")

    # Attach embeddings back to chunks (in memory only)
    for i, emb in enumerate(embeddings):
        chunks[i]["embedding_dim"] = len(emb)

    print("Embeddings created successfully")


if __name__ == "__main__":
    create_embeddings()
