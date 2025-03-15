# 📄 ESG AI Assistant - Day 4: Optimization & Retrieval Improvement

---

## **Objective**  
Students will learn how to **improve retrieval quality** by refining chunking strategies, implementing reranking models, and optimizing LLM prompting for ESG queries.

---

## **1️⃣ Theory Session (30-45 min)**

### **🔍 Optimizing Chunking & Retrieval**  
- **Impact of chunk size on retrieval accuracy**.
- **Semantic vs. fixed-length chunking**.
- **Hierarchical chunking** (breaking reports into sections/subsections).

### **📊 Reranking Strategies**  
- Why initial retrieval results might not be the most relevant.
- Implementing **reranking models** (e.g., **Cohere Reranker, BM25, Cross-Encoders**).
- Combining **vector search & traditional keyword search** for hybrid retrieval.

### **🛠️ LLM Optimization**  
- How **prompt engineering** affects answer quality.
- Using **few-shot learning** to guide the LLM.
- Implementing **retrieval constraints** (e.g., filtering by metadata, document type).

---

## **2️⃣ Practical Session (2.5 - 3 hours)**  

✅ **Task 1: Test Different Chunking Strategies**
- Compare **fixed-length** vs. **semantic** chunking on ESG reports.
- Measure retrieval accuracy using **different chunk sizes**.

✅ **Task 2: Implement a Reranker Model**
- Apply **BM25 or Cohere Reranker** to refine retrieved ESG results.
- Adjust scoring methods for **better retrieval ranking**.

✅ **Task 3: Improve LLM Answering Performance**
- Experiment with **prompt engineering techniques**.
- Apply **query expansion** and **context formatting** for more accurate responses.

---

## **🔗 GitHub Repository & Code**
📌 **[GitHub Repo - Optimization & Reranking](#)**

### **Folder Structure:**
```
├── day_4/
│   ├── day_4.md  # Course material
│   ├── data/  # ESG report chunks & retrieval logs
│   ├── notebooks/
│   │   ├── 04_optimization.ipynb  # Jupyter notebook for optimizing retrieval
│   ├── scripts/
│   │   ├── reranker.py  # Script to rerank retrieved ESG results
│   │   ├── prompt_tuning.py  # Script for optimizing LLM responses
│   ├── requirements.txt  # Python dependencies for Day 4
│   ├── README.md  # Specific instructions for Day 4
```

### **📌 Key Files:**
- `notebooks/04_optimization.ipynb` → Analyze and optimize retrieval quality.
- `scripts/reranker.py` → Implement ranking improvements for retrieval.
- `scripts/prompt_tuning.py` → Test different prompts for ESG answer generation.

---

## **🎯 Expected Outcome**  
By the end of the session, students will have a **more accurate retrieval system** that ranks results better and generates **higher-quality answers from the LLM**.

---
