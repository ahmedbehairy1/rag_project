# RAG System with Gemini LLM

## Overview
This project implements a production-style Retrieval Augmented Generation (RAG) system using the TriviaQA dataset.
The system retrieves relevant document chunks using vector similarity search (ChromaDB) and generates accurate
answers using Google's Gemini LLM.
*Due to time constraints, a subset of TriviaQA was used*

---

## Architecture
User Question  
→ Embedding  
→ Vector Search (ChromaDB)  
→ Retrieved Context  
→ Gemini LLM  
→ Final Answer  

---

## Tech Stack
- Python
- FastAPI
- SentenceTransformers
- ChromaDB
- Google Gemini API
- Docker

---

### Evaluation Graphs

#### Accuracy per Question
![Accuracy](img/accuracy_per_question.png)

#### Latency per Question
![Latency](img/latency_per_question.png)
## Setup & Run

### Local
```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
