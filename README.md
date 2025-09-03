# DiaXplain – Explainable AI for Diabetes Risk Prediction

DiaXplain is an explainable AI system designed to predict diabetes risk and provide transparent insights into the contributing health factors. It combines machine learning with interpretability methods to support both patients and healthcare practitioners in understanding the "why" behind each prediction.
________________________________________
## Repository Structure

•	diabetes/ – Main Django project folder

  &emsp;&emsp; o	diabetes/ – Core Django app with settings and configurations
 
  &emsp;&emsp; o	home/ – App handling prediction logic, views, and URLs
 
  &emsp;&emsp; o	static/ – Static files, styles, images, and saved ML artifacts
 
  &emsp;&emsp; o	templates/ – HTML templates for frontend pages

•	db.sqlite3 – Local SQLite database storing users and feedback

•	diabetes.csv – Processed dataset used for training and evaluation

•	main1.ipynb – Jupyter notebook for model training, testing, and analysis

•	manage.py – Django management script (migrations, runserver, etc.)

•	requirements.txt – List of dependencies required to run the project

____________________________________________________________________________________

## The Concept

Machine learning in healthcare often suffers from being a "black box," limiting trust and adoption. DiaXplain addresses this by combining predictive performance with interpretability.

The core question:

Can an AI system predict diabetes risk while also explaining the key health factors driving its decision?

DiaXplain predicts diabetes risk probability and provides:

•	A classification result (Diabetic / Non-Diabetic)

•	Feature-level explanations on what increased or reduced risk

•	Personalized reasoning via LIME-based interpretability
________________________________________

## System Overview

•	Methodology– Data preprocessing, outlier treatment, SMOTE class balancing, and comparative evaluation of multiple models

•	Explainability – LIME-based feature influence reports for transparent predictions

•	Performance Summaries- Accuracy, Precision, Recall, and F1-Score across tested models

•  Data Source – Pima Indians Diabetes Dataset (augmented with preprocessing and balancing; limited to women, hence not fully generalizable)

•  Deployment – Django-based web application with user authentication, prediction form, and feedback system
________________________________________

## Current Performance

Last updated: June 3rd, 2025

•	Dataset: Pima Indians Diabetes Dataset (768 samples, 9 features)

•	Preprocessing: Missing value imputation, outlier handling (IQR/Z-score), class balancing (SMOTE), scaling (StandardScaler)

•	Models Tested: Logistic Regression, Random Forest, SVM, Gradient Boosting, XGBoost, LightGBM, etc.

•	Selected Model: Extra Trees Classifier

•	Best Scores:

&emsp;&emsp;  o	Accuracy: 81%

&emsp;&emsp;  o	Precision: 75.6%

 &emsp;&emsp; o	Recall: 92.0%

 &emsp;&emsp; o	F1-Score: 83.0%
________________________________________

## Features of This Repository

•	Data preprocessing pipeline (handling missing values, outliers, and imbalance)

•	Comparison of multiple machine learning models with evaluation metrics

•	Best model (Extra Trees) saved for deployment

•	Explainable predictions using LIME for local interpretability

•	Django web app with:

&emsp;&emsp; o	User signup/login/logout functionality

&emsp;&emsp; o	Diabetes prediction form

 &emsp;&emsp; o	Explainability option for feature-level insights

 &emsp;&emsp; o	Feedback submission system
________________________________________

## Tech Stack

### Core Technologies

•	Python (pandas, numpy, scikit-learn, imbalanced-learn)

•	Django (web framework)

•	LIME (explainability)

•	Matplotlib / Seaborn (visualizations)

### Key Features

•	Robust preprocessing and resampling (SMOTE)

•	Multiple model training and evaluation pipeline

•	Model persistence using Joblib

•	Explainability-first approach (LIME)

•	Full-stack web deployment with Django
________________________________________

## System Requirements

•	Python 3.10+

•	Django 5+

•	scikit-learn, pandas, numpy, imbalanced-learn, lime, joblib

•	~50MB storage for datasets and saved models
________________________________________

## Follow Along

•	Development started: April 2025

•	Planned enhancements:

&emsp;&emsp; o	SHAP integration for global interpretability

&emsp;&emsp;  o	Cloud deployment for broader access

&emsp;&emsp;  o	Natural language explanations using LLMs
________________________________________

## Why This Matters

AI in healthcare cannot remain a black box. Trustworthy systems must provide both predictions and explanations that clinicians and patients can interpret. DiaXplain focuses on transparency, accountability, and practical decision support in diabetes risk prediction.
________________________________________

## Contact

#### For inquiries, suggestions, or collaboration:

Email: zarkahasan9@gmail.com
