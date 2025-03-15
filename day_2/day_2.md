# 📄 ESG AI Assistant - Day 2: Chunking & Retrieval

---

## **Objective**  
Students will learn how **Retrieval-Augmented Generation (RAG)** works and build a **document retrieval system** by chunking ESG reports and embedding them for efficient search.

---

## **1️⃣ Theory Session (30-45 min)**

### **🔍 LLMs & RAG Overview**  
- **Why RAG?** LLMs are powerful, but they lack access to real-time ESG data.
- **How does retrieval work?**
  - User asks a question → Retrieve relevant ESG text → Generate a response.
- **Vector Search & Embeddings:** Converting text into numerical vectors for semantic search.

### **📊 Chunking ESG Reports**  
- **Why chunking?** Full reports are too large; breaking them into sections improves retrieval.
- **Types of Chunking:**
  - **Fixed-length chunking** (splitting by word count).
  - **Semantic chunking** (splitting at headings & meaningful sections).

### **🛠️ Storing & Querying with a Vector DB**  
- **Embedding models** (e.g., `sentence-transformers` for ESG text).
- **Vector databases** (FAISS, ChromaDB) for fast document retrieval.

---

## **2️⃣ Practical Session (2.5 - 3 hours)**  

✅ **Task 1: Chunk ESG Reports**
- Use Python to split sustainability reports into **structured chunks**.
- Experiment with different chunking methods.

✅ **Task 2: Generate & Store Embeddings**
- Convert text chunks into **vector representations** using `sentence-transformers`.
- Store embeddings in FAISS for fast retrieval.

✅ **Task 3: Querying the Vector Database**
- Implement a **simple search function** that retrieves relevant ESG sections.
- Test retrieval quality by asking ESG-related questions.

---

## **🔗 GitHub Repository & Code**
📌 **[GitHub Repo - Chunking & Retrieval](#)**

### **Folder Structure:**
```
├── day_2/
│   ├── day_2.md  # Course material
│   ├── data/  # ESG reports for chunking
│   ├── notebooks/
│   │   ├── 02_chunking_retrieval.ipynb  # Jupyter notebook for chunking & retrieval
│   ├── scripts/
│   │   ├── chunking.py  # Python script for document chunking
│   │   ├── embedding.py  # Script to generate & store embeddings
│   ├── requirements.txt  # Python dependencies for Day 2
│   ├── README.md  # Specific instructions for Day 2
```

### **📌 Key Files:**
- `notebooks/02_chunking_retrieval.ipynb` → Implement chunking & retrieval.
- `scripts/chunking.py` → Script to split ESG reports into structured chunks.
- `scripts/embedding.py` → Generate & store embeddings in a vector database.
- `data/` → ESG reports for testing retrieval.

---

## **🎯 Expected Outcome**  
By the end of the session, students will have a **working ESG document retriever** that efficiently searches sustainability reports.

---
