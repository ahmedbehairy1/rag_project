#import necessary libraries
import os
from dotenv import load_dotenv
from google import genai
from app.retriever import retrieve_top_k

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Prepare context by retrieving relevant chunks
def prepare_context(question, top_k=5):
    """
    Retrieve top-k relevant chunks from the retriever and print them.
    """
    top_chunks = retrieve_top_k(question, k=top_k)
    context_text = " ".join(top_chunks)
    return context_text , top_chunks

# Generate answer using Gemini API
def generate_answer(question, context):
    """
    Generate an answer using Gemini API.
    """
    prompt = f"""You are an expert trivia assistant.
Your task is to answer the question based on the provided Context.
Answer the question directly and concisely using the provided context.
Do not mention "the context says" or "based on the information provided".
Just give the direct answer.
Rules:
1. Use the context to formulate a clear and concise answer.
2. If the answer isn't explicitly stated, use the context to make a logical inference.
3. Only if the context is completely irrelevant to the question, say "I do not know".

Context:
{context}

Question: {question}
Answer:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )
    return response.text


def answer_question(question, top_k=5):
    context_text, context_chunks = prepare_context(question, top_k=top_k)
    answer = generate_answer(question, context_text)

    return {
        "answer": answer,
        "context": context_chunks
    }

