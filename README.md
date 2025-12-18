# Mass File Plagiarism Checker (Web-Based NLP System)

A web-based plagiarism detection system designed to compare **2 to 100 files simultaneously** and generate detailed **cross-file similarity reports** using Natural Language Processing (NLP) techniques.

The application supports multiple document and source-code formats and performs efficient pairwise comparisons without redundant or self-matching operations.

---

## Features

- Upload and process **2 to 100 files in a single request**
- Supports multiple file formats:
  - Documents: `.pdf`, `.txt`, `.docx`
  - Source code: `.py`, `.java`, `.js`, `.c`, `.cpp`
- Pairwise plagiarism comparison between all distinct file combinations
- No self-comparison (a file is never compared with itself)
- No duplicate comparisons (A–B is computed once; B–A is skipped)
- Plagiarism percentage calculation for each file pair
- Web-based interface built using Flask
- NLP-based similarity detection using TF-IDF and cosine similarity

---

## System Overview

1. Uploaded files are converted into plain text using format-specific parsers
2. Text content is vectorized using TF-IDF (Term Frequency–Inverse Document Frequency)
3. Cosine similarity is computed between each unique file pair
4. Results are sorted and presented as a structured plagiarism report

This methodology is commonly used in academic and industry-grade text similarity systems.

---

## Technology Stack

### Backend
- Python
- Flask

### NLP and Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

### File Processing
- PyPDF2 for PDF extraction
- python-docx for DOCX extraction

### Frontend
- HTML
- CSS

---

## Project Structure

## Project Structure

```text
mass-plagiarism-checker/
├── app.py
├── fileReader.py
├── plagiarismEngine.py
├── requirements.txt
├── uploads/
└── templates/
    └── index.html



---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Shivam-Shukla0/mass-plagiarism-checker.git
cd mass-plagiarism-checker


pip install -r requirements.txt


python app.py


http://127.0.0.1:5000
