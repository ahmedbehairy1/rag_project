#import necessary libraries
from fastapi import FastAPI
from pydantic import BaseModel
import time
from app.llm import answer_question

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
