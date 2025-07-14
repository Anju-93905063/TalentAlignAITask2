# TalentAlign AI 💼  
**Streamlining Talent Discovery with Intelligent Resume Matching**

### 🔢 Batch - 1  
**Task Objectives:**
1. Remove extra spaces, symbols, stopwords  
2. Convert text to lowercase  
3. Replace common abbreviations (e.g., `JS` → `JavaScript`)

---

## 📌 Overview

**TalentAlign AI** is a lightweight NLP-based tool designed to help recruiters and job seekers by analyzing the textual similarity between a Resume and a Job Description (JD).  
This project uses basic Natural Language Processing techniques like text preprocessing and cosine similarity to calculate a **match score**.

---

## 🚀 Features

- 📄 Upload Resume and Job Description (in PDF format)
- 🔍 Extract and display **raw text**
- 🧹 Clean the text:
  - Remove special characters, stopwords
  - Convert to lowercase
  - Replace common abbreviations
- 📊 Show similarity score between resume and JD using **TF-IDF + Cosine Similarity**
- 🖥️ Simple web interface using Streamlit

---

## 🧠 Tech Stack

- **Python 3.10+**
- **Streamlit** – for the user interface
- **PyMuPDF (fitz)** – to extract text from PDF files
- **NLTK** – for stopword removal
- **Scikit-learn** – for TF-IDF and similarity score

---



