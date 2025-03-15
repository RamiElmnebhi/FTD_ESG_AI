import os
import pdfplumber
import nltk
import re
import json
from tqdm import tqdm

# Download necessary resources
nltk.download('punkt')

# Define paths
data_dir = "day_2/data/"
os.makedirs(data_dir, exist_ok=True)

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Function to chunk text
def chunk_text(text, chunk_size=200):
    sentences = nltk.sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_length = 0
    for sentence in sentences:
        current_chunk.append(sentence)
        current_length += len(sentence.split())
        if current_length >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

# Sample dataset (Placeholder: Replace with real ESG reports)
data_sample = [
    {"company": "TotalEnergies", "year": 2024, "file": "totalenergies_sustainability-climate-2024-progress-report_2024_en_pdf.pdf"},
]
dataframe = pd.DataFrame(data_sample)

def process_and_chunk_reports(dataframe, data_dir):
    processed_chunks = []
    for _, row in tqdm(dataframe.iterrows(), total=len(dataframe)):
        file_path = os.path.join(data_dir, row["file"])
        if os.path.exists(file_path):
            raw_text = extract_text_from_pdf(file_path)
            text_chunks = chunk_text(raw_text)
            for chunk in text_chunks:
                processed_chunks.append({
                    "company": row["company"],
                    "year": row["year"],
                    "chunk": chunk
                })
        else:
            print(f"File {row['file']} not found!")
    return processed_chunks

# Process ESG reports
processed_data = process_and_chunk_reports(dataframe, data_dir)

# Save as JSON
with open(os.path.join(data_dir, "processed_esg_chunks.json"), "w") as f:
    json.dump(processed_data, f, indent=4)

print("Chunking complete. Data saved.")
