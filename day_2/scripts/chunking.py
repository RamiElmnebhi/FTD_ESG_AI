import os
import pdfplumber
import nltk
import re
import json
from tqdm import tqdm
import logging
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from pathlib import Path

# Download necessary resources
nltk.download('punkt')

# Set up logging
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths
data_dir = "day_2/data/"
os.makedirs(data_dir, exist_ok=True)

@dataclass
class TextChunk:
    """Represents a chunk of text with metadata."""
    text: str
    start_idx: int
    end_idx: int
    metadata: Dict[str, Any]

class ESGDocumentChunker:
    """Class to handle ESG document chunking with different strategies."""
    
    def __init__(self, 
                 chunk_size: int = 500,
                 chunk_overlap: int = 50,
                 min_chunk_size: int = 100):
        """Initialize chunker with parameters.
        
        Args:
            chunk_size: Target size of chunks in words
            chunk_overlap: Number of words to overlap between chunks
            min_chunk_size: Minimum chunk size to keep
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.min_chunk_size = min_chunk_size
    
    def _split_into_sentences(self, text: str) -> List[str]:
        """Split text into sentences using regex."""
        # Basic sentence splitting - can be enhanced with better rules
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def chunk_by_fixed_size(self, text: str, metadata: Dict[str, Any]) -> List[TextChunk]:
        """Split text into fixed-size chunks with overlap."""
        sentences = self._split_into_sentences(text)
        chunks = []
        current_chunk = []
        current_size = 0
        start_idx = 0
        
        for sentence in sentences:
            sentence_words = len(sentence.split())
            
            if current_size + sentence_words > self.chunk_size and current_chunk:
                # Create chunk
                chunk_text = ' '.join(current_chunk)
                chunks.append(TextChunk(
                    text=chunk_text,
                    start_idx=start_idx,
                    end_idx=start_idx + len(chunk_text),
                    metadata=metadata.copy()
                ))
                
                # Keep overlap for next chunk
                overlap_words = ' '.join(current_chunk[-self.chunk_overlap:])
                current_chunk = []
                if overlap_words:
                    current_chunk.append(overlap_words)
                current_size = len(overlap_words.split())
                start_idx = start_idx + len(chunk_text) - len(overlap_words)
            
            current_chunk.append(sentence)
            current_size += sentence_words
        
        # Add final chunk if it meets minimum size
        if current_chunk and current_size >= self.min_chunk_size:
            final_text = ' '.join(current_chunk)
            chunks.append(TextChunk(
                text=final_text,
                start_idx=start_idx,
                end_idx=start_idx + len(final_text),
                metadata=metadata.copy()
            ))
        
        return chunks
    
    def chunk_by_section(self, text: str, metadata: Dict[str, Any]) -> List[TextChunk]:
        """Split text into chunks based on section headings."""
        # Common ESG section heading patterns
        section_patterns = [
            r'^(?:\d+\.)?\s*(?:SECTION|CHAPTER)\s+[\dA-Z]+',
            r'^(?:\d+\.)?\s*[A-Z][A-Z\s]+(?:\:|\n)',
            r'^\d+\.\d+\s+[A-Z][A-Za-z\s]+',
        ]
        
        # Combine patterns
        combined_pattern = '|'.join(f'({p})' for p in section_patterns)
        
        # Split text into sections
        sections = re.split(combined_pattern, text)
        sections = [s.strip() for s in sections if s and s.strip()]
        
        chunks = []
        current_pos = 0
        
        for section in sections:
            # Skip if section is too small
            if len(section.split()) < self.min_chunk_size:
                continue
            
            # If section is too large, split it further
            if len(section.split()) > self.chunk_size:
                sub_chunks = self.chunk_by_fixed_size(section, metadata)
                chunks.extend(sub_chunks)
            else:
                chunks.append(TextChunk(
                    text=section,
                    start_idx=current_pos,
                    end_idx=current_pos + len(section),
                    metadata=metadata.copy()
                ))
            
            current_pos += len(section)
        
        return chunks
    
    def chunk_document(self, 
                      text: str, 
                      metadata: Dict[str, Any],
                      method: str = 'fixed') -> List[TextChunk]:
        """Chunk document using specified method."""
        if method == 'fixed':
            return self.chunk_by_fixed_size(text, metadata)
        elif method == 'section':
            return self.chunk_by_section(text, metadata)
        else:
            raise ValueError(f"Unknown chunking method: {method}")

def save_chunks(chunks: List[TextChunk], output_file: Path):
    """Save chunks to JSON file."""
    chunk_data = [
        {
            'text': chunk.text,
            'start_idx': chunk.start_idx,
            'end_idx': chunk.end_idx,
            'metadata': chunk.metadata
        }
        for chunk in chunks
    ]
    
    with open(output_file, 'w') as f:
        json.dump(chunk_data, f, indent=2)
    
    logging.info(f"Saved {len(chunks)} chunks to {output_file}")

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

def main():
    """Example usage of the chunker."""
    # Example text (replace with actual ESG report)
    text = """
    1. ENVIRONMENTAL IMPACT
    Our company is committed to reducing carbon emissions...
    
    2. SOCIAL RESPONSIBILITY
    We believe in creating a diverse and inclusive workplace...
    
    3. GOVERNANCE
    Our board ensures transparency and accountability...
    """
    
    metadata = {
        'source': 'example_report.pdf',
        'year': 2024,
        'company': 'Example Corp'
    }
    
    chunker = ESGDocumentChunker()
    
    # Try both chunking methods
    fixed_chunks = chunker.chunk_document(text, metadata, method='fixed')
    section_chunks = chunker.chunk_document(text, metadata, method='section')
    
    print(f"Fixed-size chunks: {len(fixed_chunks)}")
    print(f"Section-based chunks: {len(section_chunks)}")

if __name__ == "__main__":
    main()
