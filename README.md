# DiaXplain – Explainable AI for Diabetes Risk Prediction

DiaXplain is an explainable AI system designed to predict diabetes risk and provide transparent insights into the contributing health factors. It combines machine learning with interpretability methods to support both patients and healthcare practitioners in understanding the "why" behind each prediction.
________________________________________
## Repository Structure  

&emsp;&emsp; •	diabetes/ – Main Django project folder  
&emsp;&emsp;&emsp;&emsp; o	diabetes/ – Core Django app with settings and configurations  
&emsp;&emsp;&emsp;&emsp; o	home/ – App handling prediction logic, views, and URLs  
&emsp;&emsp;&emsp;&emsp; o	static/ – Static files, styles, images, and saved ML artifacts  
&emsp;&emsp;&emsp;&emsp; o	templates/ – HTML templates for frontend pages
&emsp;&emsp;•	db.sqlite3 – Local SQLite database storing users and feedback  
&emsp;&emsp;•	diabetes.csv – Processed dataset used for training and evaluation  
&emsp;&emsp;•	main1.ipynb – Jupyter notebook for model training, testing, and analysis   
&emsp;&emsp;•	manage.py – Django management script (migrations, runserver, etc.)  
&emsp;&emsp;•	requirements.txt – List of dependencies required to run the project

____________________________________________________________________________________

## The Concept

Machine learning in healthcare often suffers from being a "black box," limiting trust and adoption. DiaXplain addresses this by combining predictive performance with interpretability. 

The core question:  
Can an AI system predict diabetes risk while also explaining the key health factors driving its decision?  

&emsp;DiaXplain predicts diabetes risk probability and provides:   
&emsp;&emsp;•	A classification result (Diabetic / Non-Diabetic)  
&emsp;&emsp;•	Feature-level explanations on what increased or reduced risk  
&emsp;&emsp;•	Personalized reasoning via LIME-based interpretability  
________________________________________

## System Overview

&emsp;&emsp;•	Methodology– Data preprocessing, outlier treatment, SMOTE class balancing, and comparative evaluation of multiple models  
&emsp;&emsp;•	Explainability – LIME-based feature influence reports for transparent predictions  
&emsp;&emsp;•	Performance Summaries- Accuracy, Precision, Recall, and F1-Score across tested models  
&emsp;&emsp;•  Data Source – Pima Indians Diabetes Dataset (augmented with preprocessing and balancing; limited to women)  
&emsp;&emsp;•  Deployment – Django-based web application with user authentication, prediction form, and feedback system
________________________________________

## Current Performance

Last updated: June 3rd, 2025  
&emsp;&emsp;•	Dataset: Pima Indians Diabetes Dataset (768 samples, 9 features)  
&emsp;&emsp;•	Preprocessing: Missing value imputation, outlier handling (IQR/Z-score), class balancing (SMOTE), scaling (StandardScaler)  
&emsp;&emsp;•	Models Tested: Logistic Regression, Random Forest, SVM, Gradient Boosting, XGBoost, LightGBM, etc.  
&emsp;&emsp;•	Selected Model: Extra Trees Classifier  
&emsp;&emsp;•	Best Scores:  
&emsp;&emsp;&emsp;&emsp; o	Accuracy: 81%  
&emsp;&emsp;&emsp;&emsp; o	Precision: 75.6%  
&emsp;&emsp;&emsp;&emsp; o	Recall: 92.0%  
&emsp;&emsp;&emsp;&emsp; o	F1-Score: 83.0%
________________________________________

## Features of This Repository

&emsp;&emsp;•	Data preprocessing pipeline (handling missing values, outliers, and imbalance)  
&emsp;&emsp;•	Comparison of multiple machine learning models with evaluation metrics  
&emsp;&emsp;•	Best model (Extra Trees) saved for deployment  
&emsp;&emsp;•	Explainable predictions using LIME for local interpretability  
&emsp;&emsp;•	Django web app with:  
&emsp;&emsp;&emsp;&emsp; o	User signup/login/logout functionality  
&emsp;&emsp;&emsp;&emsp; o	Diabetes prediction form  
&emsp;&emsp;&emsp;&emsp; o	Explainability option for feature-level insights  
&emsp;&emsp;&emsp;&emsp; o	Feedback submission system
________________________________________

## Tech Stack

### Core Technologies

&emsp;&emsp;•	Python (pandas, numpy, scikit-learn, imbalanced-learn)  
&emsp;&emsp;•	Django (web framework)  
&emsp;&emsp;•	LIME (explainability)  
&emsp;&emsp;•	Matplotlib / Seaborn (visualizations)

### Key Features

&emsp;&emsp;•	Robust preprocessing and resampling (SMOTE)  
&emsp;&emsp;•	Multiple model training and evaluation pipeline  
&emsp;&emsp;•	Model persistence using Joblib  
&emsp;&emsp;•	Explainability-first approach (LIME)  
&emsp;&emsp;•	Full-stack web deployment with Django
________________________________________

## System Requirements

&emsp;&emsp;•	Python 3.10+  
&emsp;&emsp;•	Django 5+  
&emsp;&emsp;•	scikit-learn, pandas, numpy, imbalanced-learn, lime, joblib  
&emsp;&emsp;•	~50MB storage for datasets and saved models
________________________________________

## Follow Along

&emsp;&emsp;•	Development started: April 2025  
&emsp;&emsp;•	Planned enhancements:  
&emsp;&emsp;&emsp;&emsp; o	SHAP integration for global interpretability  
&emsp;&emsp;&emsp;&emsp;  o	Cloud deployment for broader access  
&emsp;&emsp;&emsp;&emsp;  o	Natural language explanations using LLMs
________________________________________

## Why This Matters

AI in healthcare cannot remain a black box. Trustworthy systems must provide both predictions and explanations that clinicians and patients can interpret. DiaXplain focuses on transparency, accountability, and practical decision support in diabetes risk prediction.
________________________________________

## Contact

#### For inquiries, suggestions, or collaboration:

Email: zarkahasan9@gmail.com
