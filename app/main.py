# import necessary libraries
from fastapi import FastAPI
from pydantic import BaseModel
import time
from .llm import answer_question
import uvicorn
import os
from typing import List
import logging

# Configure logging
logging.basicConfig(
    filename="query_logs.log",
    level=logging.INFO,
    format="%(asctime)s - QUESTION: %(message)s"
)

# Initialize FastAPI app
app = FastAPI(title="RAG Gemini API")

# Request model
class QueryRequest(BaseModel):
    question: str
    top_k: int = 5  # number of chunks to retrieve

# Response model
class QueryResponse(BaseModel):
    answer: str
    contexts: List[str]
    latency: float

# Endpoint to handle RAG queries
@app.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):
    start_time = time.time()

    # answer_question returns a dict: {"answer": ..., "context": [...]}
    result = answer_question(
        request.question,
        top_k=request.top_k
    )

    latency = time.time() - start_time
    
    # Log the question, top_k, and latency
    logging.info(
        f"{request.question} | top_k={request.top_k} | latency={latency:.3f}s"
    )

    return QueryResponse(
        answer=result["answer"],
        contexts=result["context"],
        latency=latency
    )

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Read PORT from environment
    uvicorn.run(app, host="0.0.0.0", port=port)
