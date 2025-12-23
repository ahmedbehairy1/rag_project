#import necessary libraries
from datasets import load_dataset
import json
import os

#function to load trivia subset
def load_trivia_subset():
    dataset = load_dataset("trivia_qa", "rc", split="train[:150]")

    samples = []

    for item in dataset:
        contexts = item["entity_pages"]["wiki_context"]

        if contexts:
            samples.append({
                "question": item["question"],
                "context": contexts[0]
            })

    os.makedirs("data", exist_ok=True)

    with open("data/trivia_subset.json", "w", encoding="utf-8") as f:
        json.dump(samples, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(samples)} samples")

if __name__ == "__main__":
    load_trivia_subset()
