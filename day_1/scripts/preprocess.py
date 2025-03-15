import os
import pandas as pd
import json
import re
import nltk
import pdfplumber
import logging
from tqdm import tqdm
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from typing import Dict, List, Any

# Set up logging
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

# Download necessary resources
try:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('punkt_tab')
except Exception as e:
    logging.error(f"Error downloading NLTK resources: {e}")
    raise

# ESG-specific keywords to preserve during cleaning
ESG_KEYWORDS = {
    'environmental': ['co2', 'ghg', 'carbon', 'emission', 'renewable', 'waste', 'water'],
    'social': ['diversity', 'inclusion', 'employee', 'safety', 'community', 'human rights'],
    'governance': ['board', 'compliance', 'ethics', 'risk', 'transparency']
}

class ESGTextProcessor:
    """Class to handle ESG report text processing."""
    
    def __init__(self, data_dir: str):
        """Initialize with data directory path."""
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        self.stopwords = set(stopwords.words('english'))
        # Don't remove ESG-specific terms even if they're stopwords
        self.stopwords -= {word for category in ESG_KEYWORDS.values() for word in category}
    
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text from a PDF file with error handling."""
        try:
            text = ""
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    try:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\\n"
                    except Exception as e:
                        logging.warning(f"Error extracting text from page: {e}")
            return text
        except Exception as e:
            logging.error(f"Error processing PDF {pdf_path}: {e}")
            raise
    
    def clean_text(self, text: str) -> str:
        """Clean and preprocess extracted text while preserving ESG terms."""
        try:
            # Convert to lowercase
            text = text.lower()
            
            # Remove extra spaces
            text = re.sub(r'\\s+', ' ', text)
            
            # Preserve ESG-specific terms and metrics
            esg_pattern = r'\\d+(?:\\.\\d+)?\\s*(?:co2|ghg|kwh|mwh|tons?|percent|%)'
            esg_matches = re.finditer(esg_pattern, text)
            esg_terms = {m.group() for m in esg_matches}
            
            # Remove special characters but preserve important symbols
            text = re.sub(r'[^a-zA-Z0-9.,!?%€$]', ' ', text)
            
            # Tokenize and remove stopwords
            words = word_tokenize(text)
            words = [word for word in words if word not in self.stopwords]
            
            # Add back preserved ESG terms
            words.extend(esg_terms)
            
            return " ".join(words)
        except Exception as e:
            logging.error(f"Error cleaning text: {e}")
            raise

def process_esg_reports(dataframe: pd.DataFrame, processor: ESGTextProcessor) -> List[Dict[str, Any]]:
    """Process ESG reports from PDF to cleaned text."""
    processed_reports = []
    
    for _, row in tqdm(dataframe.iterrows(), total=len(dataframe)):
        file_path = os.path.join(processor.data_dir, row["file"])
        logging.info(f"Processing file: {file_path}")
        
        if not os.path.exists(file_path):
            logging.warning(f"File not found: {file_path}")
            continue
            
        try:
            raw_text = processor.extract_text_from_pdf(file_path)
            logging.info(f"Extracted {len(raw_text)} characters of text")
            
            cleaned_text = processor.clean_text(raw_text)
            logging.info(f"Cleaned text length: {len(cleaned_text)}")
            
            # Validate cleaned text
            if len(cleaned_text) < 100:
                logging.warning(f"Unusually short cleaned text for {file_path}")
            
            processed_reports.append({
                "company": row["company"],
                "year": row["year"],
                "cleaned_text": cleaned_text,
                "original_file": row["file"]
            })
            
        except Exception as e:
            logging.error(f"Error processing {file_path}: {e}")
            continue
    
    return processed_reports

def main():
    """Main function to run the preprocessing pipeline."""
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    data_dir = os.path.join(project_root, "day_1", "data")
    
    # Initialize processor
    processor = ESGTextProcessor(data_dir)
    
    # Sample dataset
    data_sample = [
        {
            "company": "TotalEnergies",
            "year": 2024,
            "file": "totalenergies_sustainability-climate-2024-progress-report_2024_en_pdf.pdf"
        }
    ]
    
    dataframe = pd.DataFrame(data_sample)
    logging.info("Sample ESG Dataset Loaded:")
    print(dataframe)
    
    # Process reports
    processed_data = process_esg_reports(dataframe, processor)
    
    # Save results
    output_path = os.path.join(data_dir, "processed_esg_data.json")
    try:
        with open(output_path, "w") as f:
            json.dump(processed_data, f, indent=4)
        logging.info(f"Results saved to {output_path}")
    except Exception as e:
        logging.error(f"Error saving results: {e}")
        raise

if __name__ == "__main__":
    main()
