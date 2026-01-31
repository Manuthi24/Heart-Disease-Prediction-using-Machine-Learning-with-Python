import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model & scaler
model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("❤️ Heart Disease Prediction App")

st.write("""
Enter patient details to predict the likelihood of heart disease.
""")

# Example input form
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", [0, 1])  # 0=Female, 1=Male
cp = st.number_input("Chest Pain Type (0–3)", min_value=0, max_value=3)
trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG result", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", min_value=70, max_value=220)
exang = st.selectbox("Exercise Induced Angina (0 or 1)", [0, 1])
oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox("ST Slope (0=Up,1=Flat,2=Down)", [0, 1, 2])
ca = st.number_input("Number of major vessels", min_value=0, max_value=3)
thal = st.selectbox("Thalassemia (0–3)", [0, 1, 2, 3])

if st.button("Predict"):
    features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    scaled_features = scaler.transform(features)

    prediction = model.predict(scaled_features)[0]
    proba = model.predict_proba(scaled_features)[0][1]

    st.write("### Prediction:")
    if prediction == 1:
        st.error(f"High likelihood of heart disease (Probability: {proba:.2f})")
    else:
        st.success(f"Low likelihood of heart disease (Probability: {proba:.2f})")
