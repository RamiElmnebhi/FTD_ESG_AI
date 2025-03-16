# Day 1: ESG Report Processing

## Prerequisites

⚠️ **Important: Before Running the Notebooks** ⚠️

1. Install required packages:
   ```bash
   pip install -r scripts/requirements.txt --user
   ```
2. Verify installation:
   ```python
   import pandas
   import nltk
   import pdfplumber
   import regex
   import tqdm
   import matplotlib.pyplot as plt
   import seaborn as sns
   from wordcloud import WordCloud
   print("All packages installed successfully!")
   ```

Only proceed with the notebooks after confirming all packages are installed.

This directory contains materials for Day 1 of the ESG AI Assistant course, focusing on ESG data preprocessing and analysis.

## Course Outline

### 1️⃣ Theory Session (30-45 min)

#### 🔍 AI in ESG Reporting
- **What is ESG?** Overview of Environmental, Social, and Governance factors
- **Why is ESG reporting important?** Compliance with CSRD, SFDR, GRI, SASB, TCFD regulations
- **Challenges:** Unstructured reports (PDFs), data inconsistencies, missing information
- **How AI helps:**
  - NLP to extract & summarize ESG disclosures
  - Machine Learning to predict ESG risks
  - Large Language Models (LLMs) to analyze regulatory compliance

#### 📊 ESG Data Sources
- **Publicly Available ESG Datasets:**
  - GRI Reports (Global Reporting Initiative)
  - Kaggle ESG Scores (MSCI, Sustainalytics data)
  - World Bank Sustainability Indicators
  - CDP (Carbon Disclosure Project) Reports
- **Data Formats:** Structured (CSV, JSON) vs. Unstructured (PDF, Web Data)

#### 🛠️ Preprocessing ESG Data
- Handling missing values, normalizing text, cleaning noisy reports
- Extracting text from PDFs (`pdfplumber`, `PyMuPDF`)
- Tokenization, lemmatization, and Named Entity Recognition (NER) for ESG keyword extraction

### 2️⃣ Practical Session (2.5 - 3 hours)

#### Hands-on Tasks
1. **Load & Explore ESG Data**
   - Work with sample ESG dataset
   - Inspect key ESG indicators
2. **Text Preprocessing**
   - Convert PDF reports to text
   - Apply basic NLP cleaning
   - Extract structured data
3. **ESG-Specific Processing**
   - Detect mentions of carbon emissions, net zero targets
   - Identify key ESG entities

## Directory Structure

```
├── data/                  # Sample ESG dataset and processed outputs
├── notebooks/            
│   ├── 01_esg_exploration.ipynb    # Interactive exploration of ESG concepts
│   └── 01_data_preprocessing.ipynb  # Main data preprocessing notebook
├── scripts/
│   └── preprocess.py              # Python script for ESG text extraction
└── README.md                      # This file
```

## Getting Started

1. Install required packages:
   ```bash
   pip install pandas nltk pdfplumber tqdm wordcloud matplotlib seaborn
   ```

2. Start with `notebooks/01_esg_exploration.ipynb` to:
   - Understand key ESG concepts
   - Explore ESG keywords and metrics
   - Practice data extraction techniques

3. Move to `notebooks/01_data_preprocessing.ipynb` to:
   - Process PDF reports
   - Clean and structure ESG data
   - Prepare data for analysis

## Practice Exercises

The exploration notebook includes several exercises:
1. Extract specific ESG metrics (e.g., carbon emissions, diversity statistics)
2. Create visualizations of ESG term frequencies
3. Identify and analyze ESG targets and goals

## Additional Resources

- ESG Keywords Reference: See `ESG_KEYWORDS` in `scripts/preprocess.py`
- Error Handling Examples: Check the logging implementation in `preprocess.py`
- Data Validation: Review the text validation checks in the preprocessing pipeline

## Tips for Success

1. Run notebooks cell by cell to understand each step
2. Pay attention to the ESG-specific terms preserved during cleaning
3. Use the logging output to debug any issues
4. Try the practice exercises to reinforce learning

## Expected Outcome

By the end of this session, you will have:
- Understanding of ESG reporting and its challenges
- Hands-on experience with ESG data preprocessing
- A cleaned ESG dataset ready for analysis
- Practical skills in NLP and text processing
- Foundation for building an ESG AI assistant

## Next Steps

After completing these materials, you'll be ready for Day 2, where we'll focus on building the ESG AI assistant using the processed data. 