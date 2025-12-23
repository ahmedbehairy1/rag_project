# import necessary libraries
import json
import re

INPUT_PATH = "data/trivia_subset.json"
OUTPUT_PATH = "data/trivia_chunks.json"

# function to clean text
def clean_text(text: str) -> str:
    """
    Clean text by:
    - Removing extra whitespaces
    """
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# function to chunk text
def chunk_text(text: str, chunk_size: int = 400):
    """
    Split text into chunks of fixed word length
    """
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

# main preprocess function
def preprocess():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    processed_chunks = []
    chunk_id = 0

    for item in data:
        question = item["question"]
        context = clean_text(item["context"])

        chunks = chunk_text(context)

        for chunk in chunks:
            processed_chunks.append({
                "id": chunk_id,
                "question": question,
                "text": chunk
            })
            chunk_id += 1

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(processed_chunks, f, indent=2, ensure_ascii=False)

    print(f"Created {len(processed_chunks)} chunks")


if __name__ == "__main__":
    preprocess()
