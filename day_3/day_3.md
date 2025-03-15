# 📄 ESG AI Assistant - Day 3: Querying & Generating Answers

---

## **Objective**  
Students will learn how to build a **basic ESG AI assistant** that retrieves ESG-related information and generates answers using a Language Model (LLM).

---

## **1️⃣ Theory Session (30-45 min)**

### **🔍 ESG AI Assistant Overview**  
- **Why do we need retrieval-based AI assistants?**
  - LLMs alone cannot reference external documents.
  - RAG (Retrieval-Augmented Generation) enables dynamic, document-based answering.
- **Key Components:**
  - **Retriever:** Fetches the most relevant ESG text from the vector database.
  - **LLM Generator:** Uses the retrieved text to generate an answer.
  - **Prompt Engineering:** Structures queries to optimize LLM responses.

### **📊 Querying a Vector Database**  
- **How Vector Search Works:**
  - User inputs a query → Converted into an embedding → Matched with stored ESG embeddings.
- **Query Expansion:**
  - Reformulating user queries to improve retrieval performance.
- **Combining Multiple Retrieved Chunks:**
  - Merging top-ranked chunks before passing them to the LLM.

### **🛠️ Implementing RAG for ESG Queries**  
- **Retrieve → Re-rank → Generate:**
  - **Retrieve** top-matching ESG report sections.
  - **Re-rank** results based on relevance.
  - **Generate** responses using OpenAI or Llama models.

---

## **2️⃣ Practical Session (2.5 - 3 hours)**  

✅ **Task 1: Implement Query-Based Retrieval**
- Convert **user queries into embeddings** and perform a similarity search in FAISS.
- Retrieve **relevant ESG report sections**.

✅ **Task 2: Generate Answers Using an LLM**
- Send retrieved text to **GPT-4, Llama-3, or Mistral**.
- Structure prompts to ensure high-quality ESG answers.

✅ **Task 3: Build a Simple Chat Interface**
- Create a **Flask/FastAPI** backend to accept queries.
- Develop a basic **Streamlit UI** for testing queries.

---

## **🔗 GitHub Repository & Code**
📌 **[GitHub Repo - Querying & Generation](#)**

### **Folder Structure:**
```
├── day_3/
│   ├── day_3.md  # Course material
│   ├── data/  # ESG report chunks & embeddings
│   ├── notebooks/
│   │   ├── 03_rag_pipeline.ipynb  # Jupyter notebook for querying & generation
│   ├── scripts/
│   │   ├── query_retriever.py  # Script to search ESG reports
│   │   ├── llm_generator.py  # Script to generate responses using an LLM
│   ├── app/
│   │   ├── app.py  # Flask/FastAPI for querying
│   ├── requirements.txt  # Python dependencies for Day 3
│   ├── README.md  # Specific instructions for Day 3
```

### **📌 Key Files:**
- `notebooks/03_rag_pipeline.ipynb` → Implement query-based retrieval & answer generation.
- `scripts/query_retriever.py` → Search and retrieve ESG-related text.
- `scripts/llm_generator.py` → Send retrieved text to an LLM.
- `app/app.py` → Simple API for querying ESG data.

---

## **🎯 Expected Outcome**  
By the end of the session, students will have a **fully functional ESG AI assistant prototype** that retrieves relevant ESG information and generates answers.

---
