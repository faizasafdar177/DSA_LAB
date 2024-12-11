import re
from collections import defaultdict
from typing import List, Dict

# Function to preprocess text (tokenization, lowercasing, removing punctuation)
def preprocess(text: str) -> List[str]:
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    return tokens

# Function to build an inverted index
def build_index(documents: List[str]) -> Dict[str, List[int]]:
    index = defaultdict(list)
    for i, doc in enumerate(documents):
        tokens = preprocess(doc)
        for token in tokens:
            index[token].append(i)
    return index

# Function to calculate Jaccard similarity
def jaccard_similarity(doc1: List[str], doc2: List[str]) -> float:
    set1, set2 = set(doc1), set(doc2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

# Function to detect plagiarism between documents
def detect_plagiarism(documents: List[str], threshold: float = 0.5) -> List[tuple]:
    index = build_index(documents)
    similarities = []
    for i in range(len(documents)):
        for j in range(i + 1, len(documents)):
            doc1_tokens = preprocess(documents[i])
            doc2_tokens = preprocess(documents[j])
            similarity = jaccard_similarity(doc1_tokens, doc2_tokens)
            if similarity >= threshold:
                similarities.append((i, j, similarity))
    return similarities

# Main program
if __name__ == "__main__":
    docs = [
        "This is a sample document.",
        "This document is a sample example.",
        "Another example document is here.",
        "Here is a different document altogether."
    ]

    results = detect_plagiarism(docs, threshold=0.3)
    
    if results:
        for result in results:
            print(f"Documents {result[0]} and {result[1]} have a similarity of {result[2]:.2f}")
    else:
        print("No plagiarism detected.")
