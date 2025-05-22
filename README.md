# 🏦 Loan Approval Prediction System

This project is a **machine learning-based loan approval prediction system** built with:

- **Flask API** for backend processing
- **HTML frontend** for user interaction
- **RandomForestClassifier** and other ML models for classification

The system allows users to input loan-related details and receive a prediction on whether the loan will be approved or not.

---

## 🚀 Features

- Loan approval prediction using trained ML models
- Flask API for model inference
- HTML form interface for user input
- File upload support (e.g., CIBIL documents)
- Multiple models evaluated for comparison
- Model performance metrics and evaluation

---

## 📊 Model Performance

### Final Selected Model: `RandomForestClassifier`

**Accuracy:** 97.81%  
**ROC-AUC Score:** 0.9985

**Confusion Matrix:**


**Classification Report:**

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| 0     | 0.98      | 0.97   | 0.98     |
| 1     | 0.98      | 0.99   | 0.99     |

---

## 🖼 Frontend Preview

A simple form interface is provided in the `templates/loan_form.html` file. Users can enter:
- Number of Dependents
- Education Level
- Employment Type
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Total Assets
- CIBIL Document Upload

---

## 🛠 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/jahid1066/Loan-Approval-Prediction.git
cd Loan-Approval-Prediction

## Create a activate a virtual environment

python -m venv venv
venv\Scripts\activate  # On Windows
# Or
source venv/bin/activate  # On Linux/macOS

## Install dependencies

pip install -r requirements.txt


## Run the Flask application

python api.py


## Open in browser 

Visit http://127.0.0.1:5000 to view the form.