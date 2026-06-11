# Heart Disease Prediction - Simple Frontend + Backend

This is a simple full-stack version of the Heart Disease Prediction project.

## Tech Stack

- Backend: Python, FastAPI, Scikit-learn, Pandas, Joblib
- Frontend: React, Vite, CSS
- Model: Logistic Regression pipeline with StandardScaler

## Final Project Structure

```text
Heart-Disease-Prediction-using-Machine-Learning-with-Python/
├── data/
│   └── heart_disease_data.csv
├── backend/
│   ├── main.py
│   ├── train_model.py
│   ├── requirements.txt
│   └── models/
│       └── heart_model.pkl
├── frontend/
│   ├── index.html
│   ├── package.json
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       └── styles.css
└── README.md
```

## Step 1: Add these folders to your existing GitHub project

Copy the `backend` and `frontend` folders into your existing repository.

Your dataset should be available in one of these locations:

```text
data/heart_disease_data.csv
```

or

```text
data/heart.csv
```

## Step 2: Run Backend

Open terminal in the `backend` folder:

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python train_model.py
uvicorn main:app --reload
```

Backend will run here:

```text
http://localhost:8000
```

API documentation:

```text
http://localhost:8000/docs
```

## Step 3: Run Frontend

Open another terminal in the `frontend` folder:

```bash
cd frontend
npm install
npm run dev
```

Frontend will run here:

```text
http://localhost:5173
```

## API Endpoint

### POST `/predict`

Example request:

```json
{
  "age": 50,
  "sex": 1,
  "cp": 0,
  "trestbps": 120,
  "chol": 200,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 1,
  "ca": 0,
  "thal": 2
}
```

Example response:

```json
{
  "prediction": 0,
  "result": "No heart disease risk detected",
  "probability": 0.23,
  "probability_percent": 23.0,
  "risk_level": "Low",
  "note": "This is a machine learning prediction, not a medical diagnosis. Please consult a qualified doctor for real medical advice."
}
```

## Important Note

This app is for educational and portfolio purposes only. It should not be used as a real medical diagnosis system.
