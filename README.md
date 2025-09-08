# DiaXplain – Explainable AI for Diabetes Risk Prediction

  
DiaXplain is an explainable AI system designed to predict diabetes risk and provide transparent insights into the contributing health factors. It combines machine learning with interpretability methods to support both patients and healthcare practitioners in understanding the "why" behind each prediction.

## Concept
Machine learning in healthcare often suffers from being a "black box," limiting trust and adoption.  
DiaXplain addresses this by combining predictive performance with interpretability.

Core Question:  
Can an AI system predict diabetes risk while also explaining the key health factors driving its decision?

DiaXplain provides:
- A classification result (Diabetic / Non-Diabetic)  
- Feature-level explanations on what increased or reduced risk  
- Personalized reasoning via LIME-based interpretability  

---

## System Overview
- Methodology – Data preprocessing, outlier handling, SMOTE class balancing, evaluation of multiple ML models  
- Explainability – LIME-based feature influence reports for transparent predictions  
- Performance Summaries – Accuracy, Precision, Recall, and F1-Score across tested models  
- Data Source – Pima Indians Diabetes Dataset (preprocessed and balanced; limited to women)  
- Deployment – Django-based web application with:
  - User authentication  
  - Prediction form  
  - Feedback system  

---

## Current Performance
Last updated: June 3rd, 2025

- Dataset: 768 samples, 9 features  
- Preprocessing: Missing value imputation, outlier handling (IQR/Z-score), class balancing, scaling  
- Models Tested: Logistic Regression, Random Forest, SVM, Gradient Boosting, XGBoost, LightGBM, etc.  
- Selected Model: Extra Trees Classifier  

Best Scores:
- Accuracy: 81%  
- Precision: 75.6%  
- Recall: 92.0%  
- F1-Score: 83.0%  

---

## Tech Stack
### Core Technologies
- Python (pandas, numpy, scikit-learn)  
- Django (web framework)  
- LIME (explainability)  

### Key Features
- Robust preprocessing and SMOTE resampling  
- Multiple model training and evaluation pipeline  
- Model persistence using Joblib  
- Explainability-first approach with LIME  
- Full-stack deployment using Django  

---

## System Requirements
- Python 3.10+  
- Django 5+  
- scikit-learn, pandas, numpy, imbalanced-learn, lime, joblib  
- ~50MB storage for datasets and saved models  

---

## Follow Along
- Development started: April 2025  
- Planned Enhancements:
  - SHAP integration for global interpretability  
  - Cloud deployment for broader access  
  - Natural language explanations using LLMs  

---

## Why This Matters
AI in healthcare cannot remain a black box.  
Trustworthy systems must provide both predictions and explanations that clinicians and patients can interpret.  

DiaXplain focuses on transparency, accountability, and practical decision support in diabetes risk prediction.

---

## Contact
For inquiries, suggestions, or collaboration:  
Email: zarkahasan9@gmail.com
