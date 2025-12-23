#import necessary libraries
from fastapi import FastAPI
from pydantic import BaseModel
import time
from app.llm import answer_question
import uvicorn
import os

# Initialize FastAPI app
app = FastAPI(title="RAG Gemini API")

class QueryRequest(BaseModel):
    question: str
    top_k: int = 5  # number of chunks to retrieve

class QueryResponse(BaseModel):
    answer: str
    latency: float

# Endpoint to handle RAG queries
@app.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):
    start_time = time.time()

    answer = answer_question(request.question, top_k=request.top_k)

    latency = time.time() - start_time

    return QueryResponse(answer=answer, latency=latency)

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Read PORT from environment
    uvicorn.run(app, host="0.0.0.0", port=port)
