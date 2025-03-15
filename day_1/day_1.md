# 📄 ESG AI Assistant - Day 1: AI in ESG Reporting & Data Preprocessing  

---

## **Objective**  
Students will learn how **AI is transforming ESG reporting** and get hands-on with **ESG data collection & preprocessing**.

---

## **1️⃣ Theory Session (30-45 min)**

### **🔍 AI in ESG Reporting**  
- **What is ESG?** Overview of Environmental, Social, and Governance factors.
- **Why is ESG reporting important?** Compliance with **CSRD, SFDR, GRI, SASB, TCFD** regulations.
- **Challenges:** Unstructured reports (PDFs), data inconsistencies, missing information.
- **How AI helps:**
  - NLP to **extract & summarize ESG disclosures**.
  - Machine Learning to **predict ESG risks**.
  - Large Language Models (LLMs) to **analyze regulatory compliance**.

### **📊 ESG Data Sources**  
- **Publicly Available ESG Datasets:**
  - **GRI Reports** *(Global Reporting Initiative)*
  - **Kaggle ESG Scores** *(MSCI, Sustainalytics data)*
  - **World Bank Sustainability Indicators**
  - **CDP (Carbon Disclosure Project) Reports**
- **Data Formats:** Structured (CSV, JSON) vs. Unstructured (PDF, Web Data).

### **🛠️ Preprocessing ESG Data**  
- Handling **missing values, normalizing text, cleaning noisy reports**.
- Extracting text from **PDFs** (`pdfplumber`, `PyMuPDF`).
- Tokenization, lemmatization, and Named Entity Recognition (NER) for **ESG keyword extraction**.

---

## **2️⃣ Practical Session (2.5 - 3 hours)**  

✅ **Task 1: Load & Explore ESG Data**
- Students will work with a **sample ESG dataset**.
- Inspect key ESG indicators (carbon footprint, workforce diversity, governance policies).

✅ **Task 2: Text Preprocessing**
- Convert **PDF reports to text**.
- Apply **basic NLP cleaning** (removing stopwords, lowercasing, tokenization).
- Extract structured ESG data from raw text.

✅ **Task 3: ESG-Specific NLP Processing**
- Detect mentions of **carbon emissions, net zero targets, diversity policies**.
- Identify key ESG entities with **Named Entity Recognition (NER)**.

---

## **🔗 GitHub Repository & Code**
📌 **[GitHub Repo - ESG Data Preprocessing](#)**

### **Folder Structure:**
```
├── data/                  # Sample ESG dataset
├── notebooks/
│   ├── 01_data_preprocessing.ipynb  # ESG data loading & cleaning
├── scripts/
│   ├── preprocess.py       # Python script for ESG text extraction
├── requirements.txt        # Python dependencies
└── README.md               # Instructions
```

### **📌 Key Files:**
- `notebooks/01_data_preprocessing.ipynb` → Load & clean ESG data.
- `scripts/preprocess.py` → Extract & normalize text from ESG reports.
- `data/` → Example ESG dataset.

---

## **🎯 Expected Outcome**  
By the end of the session, students will have a **cleaned ESG dataset** ready for retrieval and analysis in the next class.

---
