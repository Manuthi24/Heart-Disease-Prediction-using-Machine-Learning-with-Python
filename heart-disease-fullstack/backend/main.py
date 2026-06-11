from pathlib import Path
from typing import Literal

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

APP_TITLE = "Heart Disease Prediction API"
MODEL_PATH = Path("models/heart_model.pkl")

FEATURE_COLUMNS = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]

app = FastAPI(
    title=APP_TITLE,
    description="Simple FastAPI backend for heart disease prediction.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PatientInput(BaseModel):
    age: int = Field(..., ge=1, le=120, description="Age in years")
    sex: Literal[0, 1] = Field(..., description="0 = Female, 1 = Male")
    cp: int = Field(..., ge=0, le=3, description="Chest pain type")
    trestbps: int = Field(..., ge=80, le=220, description="Resting blood pressure")
    chol: int = Field(..., ge=100, le=700, description="Serum cholesterol")
    fbs: Literal[0, 1] = Field(..., description="Fasting blood sugar > 120 mg/dl")
    restecg: int = Field(..., ge=0, le=2, description="Resting ECG result")
    thalach: int = Field(..., ge=60, le=230, description="Maximum heart rate achieved")
    exang: Literal[0, 1] = Field(..., description="Exercise induced angina")
    oldpeak: float = Field(..., ge=0, le=10, description="ST depression")
    slope: int = Field(..., ge=0, le=2, description="ST slope")
    ca: int = Field(..., ge=0, le=4, description="Number of major vessels")
    thal: int = Field(..., ge=0, le=3, description="Thalassemia value")


def load_model():
    if not MODEL_PATH.exists():
        raise HTTPException(
            status_code=500,
            detail="Model file not found. Run `python train_model.py` inside the backend folder first.",
        )
    return joblib.load(MODEL_PATH)


@app.get("/")
def root():
    return {
        "message": "Heart Disease Prediction API is running",
        "docs": "/docs",
        "predict_endpoint": "/predict",
    }


@app.get("/health")
def health_check():
    return {"status": "ok", "model_exists": MODEL_PATH.exists()}


@app.post("/predict")
def predict_heart_disease(payload: PatientInput):
    model = load_model()

    input_df = pd.DataFrame([payload.model_dump()], columns=FEATURE_COLUMNS)

    try:
        prediction = int(model.predict(input_df)[0])

        probability = None
        if hasattr(model, "predict_proba"):
            probability = float(model.predict_proba(input_df)[0][1])

    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(exc)}")

    if probability is None:
        risk_level = "High" if prediction == 1 else "Low"
    elif probability >= 0.7:
        risk_level = "High"
    elif probability >= 0.4:
        risk_level = "Moderate"
    else:
        risk_level = "Low"

    return {
        "prediction": prediction,
        "result": "Heart disease risk detected" if prediction == 1 else "No heart disease risk detected",
        "probability": probability,
        "probability_percent": round(probability * 100, 2) if probability is not None else None,
        "risk_level": risk_level,
        "note": "This is a machine learning prediction, not a medical diagnosis. Please consult a qualified doctor for real medical advice.",
    }
