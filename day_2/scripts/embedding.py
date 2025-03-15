import os
import json
import logging
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Union
from dataclasses import dataclass
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class EmbeddedChunk:
    text: str
    embedding: np.ndarray
    metadata: Dict[str, Any]

class ESGEmbeddingManager:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """Initialize the embedding manager with a sentence transformer model."""
        self.model = SentenceTransformer(model_name)
        self.chunks: List[EmbeddedChunk] = []
        self.embeddings: np.ndarray = None

    def generate_embeddings(self, texts: List[str], batch_size: int = 32) -> np.ndarray:
        """Generate embeddings for a list of texts."""
        logger.info(f"Generating embeddings for {len(texts)} texts")
        embeddings = []
        
        for i in tqdm(range(0, len(texts), batch_size)):
            batch = texts[i:i + batch_size]
            batch_embeddings = self.model.encode(batch)
            embeddings.extend(batch_embeddings)
        
        return np.array(embeddings)

    def add_chunks(self, chunks: List[EmbeddedChunk]):
        """Add chunks to the manager and update embeddings matrix."""
        self.chunks.extend(chunks)
        if self.embeddings is None:
            self.embeddings = np.array([chunk.embedding for chunk in chunks])
        else:
            new_embeddings = np.array([chunk.embedding for chunk in chunks])
            self.embeddings = np.vstack([self.embeddings, new_embeddings])

    def search(self, query: str, k: int = 3) -> List[Dict[str, Any]]:
        """Search for similar chunks using cosine similarity."""
        # Generate query embedding
        query_embedding = self.model.encode([query])[0]
        
        # Calculate similarities
        similarities = cosine_similarity([query_embedding], self.embeddings)[0]
        
        # Get top k indices
        top_k_indices = np.argsort(similarities)[-k:][::-1]
        
        # Format results
        results = []
        for idx in top_k_indices:
            results.append({
                'text': self.chunks[idx].text,
                'metadata': self.chunks[idx].metadata,
                'score': float(similarities[idx])
            })
        
        return results

    def save_data(self, file_path: Union[str, Path]):
        """Save chunks and embeddings to a file."""
        data = {
            'chunks': [
                {
                    'text': chunk.text,
                    'metadata': chunk.metadata,
                    'embedding': chunk.embedding.tolist()
                }
                for chunk in self.chunks
            ]
        }
        
        with open(file_path, 'w') as f:
            json.dump(data, f)
        
        logger.info(f"Saved data to {file_path}")

    def load_data(self, file_path: Union[str, Path]):
        """Load chunks and embeddings from a file."""
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        self.chunks = []
        embeddings = []
        
        for chunk_data in data['chunks']:
            chunk = EmbeddedChunk(
                text=chunk_data['text'],
                embedding=np.array(chunk_data['embedding']),
                metadata=chunk_data['metadata']
            )
            self.chunks.append(chunk)
            embeddings.append(chunk.embedding)
        
        self.embeddings = np.array(embeddings)
        logger.info(f"Loaded {len(self.chunks)} chunks from {file_path}")

def main():
    # Example usage
    manager = ESGEmbeddingManager()
    
    # Example texts
    texts = [
        "ESG reporting focuses on environmental impact",
        "Companies must disclose carbon emissions",
        "Social responsibility in corporate governance"
    ]
    
    # Generate embeddings
    embeddings = manager.generate_embeddings(texts)
    
    # Create chunks
    chunks = [
        EmbeddedChunk(text=text, embedding=emb, metadata={'index': i})
        for i, (text, emb) in enumerate(zip(texts, embeddings))
    ]
    
    # Add chunks to manager
    manager.add_chunks(chunks)
    
    # Try a search
    results = manager.search("carbon footprint", k=2)
    for i, result in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(f"Text: {result['text']}")
        print(f"Score: {result['score']:.3f}")

if __name__ == "__main__":
    main() 