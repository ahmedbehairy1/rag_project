# import necessary libraries
import os
import chromadb
from sentence_transformers import SentenceTransformer

# Define paths and constants
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PERSIST_DIR = os.path.join(BASE_DIR, "chroma_db")
COLLECTION_NAME = "trivia_chunks"


print("Initializing Embedding Model and Vector Store...")

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path=PERSIST_DIR)
collection = chroma_client.get_collection(name=COLLECTION_NAME)
# Function to retrieve top-k relevant chunks
def retrieve_top_k(question: str, k: int = 3):
    """
   Retrieve the best results using pre-loaded models.
    """
    
    query_embedding = embedding_model.encode(question).tolist()

    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    
    return results["documents"][0]
# Test the retriever
if __name__ == "__main__":
    test_question = "Which city hosted the 1996 Summer Olympics?"
    docs = retrieve_top_k(test_question)
    print(f"\nQuestion: {test_question}")
    for i, doc in enumerate(docs, 1):
        print(f"\nResult {i}: {doc[:200]}...")