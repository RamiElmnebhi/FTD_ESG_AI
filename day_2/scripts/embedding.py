import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Define paths
data_dir = "day_2/data/"
os.makedirs(data_dir, exist_ok=True)

# Load processed ESG text chunks
chunks_file = os.path.join(data_dir, "processed_esg_chunks.json")
if not os.path.exists(chunks_file):
    raise FileNotFoundError("Chunked ESG data file not found. Run chunking.py first.")

with open(chunks_file, "r") as f:
    processed_data = json.load(f)

# Embedding Model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert text chunks into embeddings
text_chunks = [entry["chunk"] for entry in processed_data]
embeddings = model.encode(text_chunks, convert_to_numpy=True)

# Store in FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)
faiss.write_index(index, os.path.join(data_dir, "faiss_index.bin"))

print("Embedding storage complete. FAISS index saved.")
