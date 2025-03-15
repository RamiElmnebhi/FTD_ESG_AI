# 📄 ESG AI Assistant - Day 5: Evaluation & Final Presentation

---

## **Objective**  
Students will learn how to **evaluate** their ESG AI assistant using RAG-specific metrics and will prepare their final presentations.

---

## **1️⃣ Theory Session (30-45 min)**

### **🔍 Evaluating RAG Systems**  
- **Why evaluation matters:** Ensuring retrieval accuracy & response quality.
- **Common issues:** Hallucinations, incorrect citations, irrelevant retrieval.

### **📊 RAG-Specific Evaluation Metrics**  
- **Retrieval Accuracy:** How well the system finds the correct ESG information.
- **Faithfulness (Citations Check):** Does the LLM use retrieved information?
- **Context Relevance:** Are retrieved chunks relevant to the query?
- **Response Coherence:** Does the LLM generate structured, meaningful answers?

### **🛠️ Evaluation Frameworks**  
- **RAGAs (Retrieval-Augmented Generation Assessment):**
  - Uses retrieval and answer-based metrics to evaluate ESG AI assistants.
- **Other evaluation methods:** BLEU, ROUGE, GPT-based scoring.

---

## **2️⃣ Practical Session (2.5 - 3 hours)**  

✅ **Task 1: Implement Automated RAG Evaluation**
- Use RAGAs to **measure retrieval accuracy & faithfulness**.
- Compare **retrieval-based answering vs. direct LLM responses**.

✅ **Task 2: Human Evaluation of ESG AI Responses**
- Test the AI assistant by asking **real ESG-related questions**.
- Manually check **whether responses are correct & useful**.

✅ **Task 3: Final Project Presentation**
- Each group presents **their ESG AI assistant**.
- Explain **retrieval strategies, LLM prompts, optimizations & evaluation results**.

---

## **🔗 GitHub Repository & Code**
📌 **[GitHub Repo - Evaluation & Presentation](#)**

### **Folder Structure:**
```
├── day_5/
│   ├── day_5.md  # Course material
│   ├── data/  # Evaluation datasets & logs
│   ├── notebooks/
│   │   ├── 05_evaluation.ipynb  # Jupyter notebook for RAG evaluation
│   ├── scripts/
│   │   ├── evaluate.py  # Script for automated evaluation using RAGAs
│   ├── requirements.txt  # Python dependencies for Day 5
│   ├── README.md  # Specific instructions for Day 5
```

### **📌 Key Files:**
- `notebooks/05_evaluation.ipynb` → Implement retrieval & LLM evaluation.
- `scripts/evaluate.py` → Use RAGAs for scoring ESG AI assistant.
- `data/` → Store evaluation results & examples.

---

## **🎯 Expected Outcome**  
By the end of the session, students will have **evaluated their ESG AI assistant** and presented their findings.

---