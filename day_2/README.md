# Day 2: Building an ESG Document Retrieval System

## Prerequisites

⚠️ **Important: Before Running the Notebooks** ⚠️

1. Install required packages:
   ```bash
   pip install -r scripts/requirements.txt --user
   ```
2. Verify installation:
   ```python
   import sentence_transformers
   import sklearn
   import numpy
   import pandas
   import tqdm
   import nltk
   print("All packages installed successfully!")
   ```

Only proceed with the notebooks after confirming all packages are installed.

This directory contains materials for Day 2 of the ESG AI Assistant course, focusing on document chunking, embeddings, and retrieval.

## Course Outline

### 1️⃣ Theory Session (30-45 min)

#### 🔍 LLMs & RAG Overview
- **Why RAG (Retrieval-Augmented Generation)?**
  - Limitations of LLMs with real-time ESG data
  - Benefits of combining LLMs with document retrieval
  - Architecture of RAG systems
- **Components of RAG:**
  - Document chunking and preprocessing
  - Embedding generation
  - Vector similarity search
  - LLM-based response generation

#### 📊 Document Chunking Strategies
- **Fixed-length Chunking**
  - Word count-based splitting
  - Overlap strategies
  - Pros and cons
- **Semantic Chunking**
  - Section-based splitting
  - Heading detection
  - Maintaining context
- **ESG-specific Considerations**
  - Preserving metric context
  - Handling tables and figures
  - Maintaining regulatory references

#### 🛠️ Vector Embeddings & Search
- **Embedding Models**
  - Overview of sentence-transformers
  - ESG-specific embedding considerations
  - Model selection criteria
- **Vector Similarity Search**
  - Cosine similarity implementation
  - Efficient batch processing
  - Query optimization

### 2️⃣ Practical Session (2.5 - 3 hours)

#### Hands-on Tasks
1. **Document Chunking Implementation**
   - Implement multiple chunking strategies
   - Evaluate chunk quality
   - Handle edge cases
2. **Embedding Generation**
   - Set up sentence-transformers
   - Generate and validate embeddings
   - Implement batch processing
3. **Search System Development**
   - Implement vector similarity search
   - Build efficient storage system
   - Test with ESG queries

## Directory Structure

```
├── data/                  # Processed ESG reports and embeddings
├── notebooks/            
│   └── 02_chunking_retrieval.ipynb  # Main implementation notebook
├── scripts/
│   ├── chunking.py       # Document chunking implementation
│   └── embedding.py      # Embedding generation and search
└── README.md             # This file
```

## Getting Started

1. Install required packages:
   ```bash
   pip install -r scripts/requirements.txt
   ```

2. Work through `notebooks/02_chunking_retrieval.ipynb`:
   - Implement document chunking
   - Generate and store embeddings
   - Build search functionality

## Practice Exercises

The notebook includes several exercises:
1. Implement different chunking strategies
2. Compare embedding model performance
3. Build and evaluate search queries
4. Optimize retrieval quality

## Additional Resources

- Chunking Utilities: See `scripts/chunking.py`
- Embedding Tools: Check `scripts/embedding.py`
- Vector Search Examples: Review the notebook sections on cosine similarity

## Tips for Success

1. Start with small document samples
2. Test different chunk sizes
3. Validate embedding quality
4. Use ESG-specific test queries
5. Monitor memory usage with large datasets

## Expected Outcome

By the end of this session, you will have:
- Working document chunking system
- Efficient embedding pipeline
- Vector similarity search functionality
- Understanding of RAG architecture
- Practical experience with semantic search

## Next Steps

After completing these materials, you'll be ready for Day 3, where we'll integrate this retrieval system with an LLM to build a complete ESG AI assistant. 