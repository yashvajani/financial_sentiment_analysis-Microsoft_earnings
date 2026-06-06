# Financial Sentiment Analysis - Microsoft Earnings Reports

This repository contains a comprehensive sentiment analysis pipeline for analyzing Microsoft's quarterly earnings reports. The project uses advanced natural language processing techniques and transformer-based models to extract and classify sentiment from financial documents.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
- [Models](#models)
- [Results & Analysis](#results--analysis)
- [Contributing](#contributing)

## Overview

This project analyzes the sentiment and tone of Microsoft's quarterly earnings release documents to understand market sentiment and correlate financial language with earnings per share (EPS) estimates. The analysis operates at both sentence and paragraph levels, providing granular insights into how Microsoft communicates financial performance.

### Key Objectives

- Extract textual and financial data from Microsoft earnings press releases
- Preprocess and clean financial text for sentiment analysis
- Apply multiple transformer-based sentiment classifiers
- Correlate sentiment patterns with financial metrics (EPS)
- Provide comprehensive analysis across different granularity levels (sentences vs. paragraphs)

## Project Structure
financial_sentiment_analysis-Microsoft_earnings/ 
├── code/ │ 
├── extractData.py # Data extraction from Word documents │
├── text_preprocessing.py # Text cleaning and normalization │
├── classifiers.py # Sentiment classification models │
├── explorer_sentence.ipynb # Sentence-level analysis notebook │
├── explorer_paragraph.ipynb # Paragraph-level analysis notebook 

├── data/ │ 
├── earningsrelease/ # Microsoft earnings press releases (DOCX) │
├── earnings_per_share_estimates.xlsx # EPS data │ 
└── steffen_extract_msft.csv # Extracted earnings data 
└── README.md



## Key Features

### Multi-Level Analysis
- **Sentence-Level**: Granular sentiment analysis at sentence granularity
- **Paragraph-Level**: Broader sentiment patterns at paragraph granularity
- **Financial Metrics**: Integration of EPS and financial data

### Multiple Sentiment Classifiers
- **FinBERT (Tone)**: FinBERT model fine-tuned for financial tone analysis
- **FinBERT (Classification)**: Alternative FinBERT variant for sentiment classification
- **DistilRoBERTa**: Lightweight RoBERTa model fine-tuned on financial news sentiment

### Comprehensive Text Processing
- Text lowercasing and normalization
- Unicode removal
- Lemmatization
- Stopword removal
- Configurable preprocessing pipeline

## Data

### Source Documents
The `data/earningsrelease/` directory contains Microsoft's quarterly earnings press releases in Word format (.docx), following the naming convention: `PressReleaseFYXXQX` where:
- XX = Fiscal year
- X = Quarter number

### Data Files

| File | Description |
|------|-------------|
| `earnings_per_share_estimates.xlsx` | Historical EPS estimates and actuals for Microsoft |
| `steffen_extract_msft.csv` | Pre-extracted earnings data from Microsoft releases |

### Data Extraction
The `extractData.py` module supports extraction at multiple levels:
- **Sentence-level**: Individual sentences with position metadata
- **Paragraph-level**: Full paragraphs with position metadata
- **Financial tables**: EPS data and other tabular financial information

## Installation

### Requirements
- Python 3.7+
- Jupyter Notebook (for analysis notebooks)

### Dependencies
```bash
pip install pandas numpy spacy torch transformers scikit-learn
python -m spacy download en_core_web_sm
