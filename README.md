# 🫀 Heart Disease Prediction using Machine Learning with Python

This project uses machine learning to predict the presence of heart disease in patients based on clinical data. It demonstrates the full data science workflow — from data preprocessing and model training to prediction and evaluation.

---

## 📊 Project Overview

Heart disease is one of the leading causes of death worldwide. Predicting the likelihood of heart disease using machine learning can help with early detection and preventive healthcare.

This repository contains:
- Data preprocessing and exploration using Python
- Multiple machine learning models for classification
- Training and evaluation of models
- (Optional) Deployment using a web app or command‑line interface

---

## 🗂 Repository Contents

```
📁 data/ # Dataset folder
├── heart.csv # Heart disease data (UCI/Kaggle)
📁 models/ # Saved ML models (optional)
├── model.pkl # Trained classifier model
📄 train_model.py # Script to train the model
📄 app.py # (Optional) Streamlit/Flask app for deployment
📄 requirements.txt # Required packages
📄 README.md # Project documentation

```
---

## 📌 Dataset Description

This project typically uses the **UCI Heart Disease dataset** or a similar heart disease dataset from Kaggle, containing features such as:

| Feature | Description |
|---------|-------------|
| age | Age in years |
| sex | 0 = female, 1 = male |
| cp | Chest pain type |
| trestbps | Resting blood pressure |
| chol | Serum cholesterol level |
| fbs | Fasting blood sugar > 120 mg/dl |
| restecg | Resting ECG result |
| thalach | Maximum heart rate achieved |
| exang | Exercise induced angina |
| oldpeak | ST depression induced by exercise |
| slope | Slope of the peak exercise ST segment |
| ca | Number of major vessels |
| thal | Thalassemia indicator |
| target | 0 = no heart disease, 1 = heart disease |

(Dataset format may vary depending on source.) :contentReference[oaicite:1]{index=1}

---

## 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/Manuthi24/Heart-Disease-Prediction-using-Machine-Learning-with-Python
cd Heart-Disease-Prediction-using-Machine-Learning-with-Python
```
---
Create a virtual environment and install dependencies:

```
python -m venv venv
venv\Scripts\activate         # Windows
source venv/bin/activate      # macOS/Linux

pip install -r requirements.txt

```
## 📈 Train the Model

If the project contains a training script (train_model.py), run:
```
python train_model.py

```
---
##🚀 Run Prediction App (Optional)

If the repository includes a web interface (Streamlit or Flask), launch it using:

Streamlit
```
streamlit run app.py
```
Flask
```
python app.py
```

---
Then open the app in your browser (e.g., http://localhost:8501 for Streamlit).







