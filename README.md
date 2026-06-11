![Python](https://img.shields.io/badge/Python-Machine%20Learning-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Supervised%20Learning-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Modeling-yellow)
![Data Visualization](https://img.shields.io/badge/Data--Visualization-red)
![EDA](https://img.shields.io/badge/EDA-Exploratory%20Data%20Analysis-lightgrey)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-teal)
![React](https://img.shields.io/badge/React-Frontend-blue)
![Model Deployment](https://img.shields.io/badge/Deployment-Ready%20App-orange)
![Healthcare Analytics](https://img.shields.io/badge/Healthcare-Analytics--ML-purple)
![Portfolio Project](https://img.shields.io/badge/Type-Portfolio%20Project-important)

# 🫀 Heart Disease Prediction System using Machine Learning

A full-stack machine learning web application that predicts the possibility of heart disease based on patient health-related inputs.
This project combines **Machine Learning**, **FastAPI backend**, and **React frontend** to create a simple and user-friendly prediction system.

---

## 📊 Project Overview

Heart disease is one of the most common health problems worldwide. Early prediction can help support awareness and preventive healthcare decisions.

This project uses machine learning to analyze clinical data and predict whether a patient may have a risk of heart disease. Users can enter health-related details through the frontend, and the trained model returns a prediction result with a risk level and probability.

This project demonstrates an end-to-end machine learning workflow, including:

* Data preprocessing
* Exploratory Data Analysis
* Model training
* Model evaluation
* Backend API development
* Frontend development
* ML model integration with a web application

> ⚠️ **Medical Disclaimer:**
> This project is created for educational and portfolio purposes only. It should not be used as a replacement for professional medical advice, diagnosis, or treatment.

---

## 🚀 Features

* Predicts heart disease risk using machine learning
* Uses supervised learning classification
* Clean and simple React frontend
* FastAPI backend for prediction requests
* Trained model using Scikit-learn
* Real-time prediction from user input
* Displays prediction result clearly
* Shows risk level and probability
* Beginner-friendly full-stack project structure
* Suitable for academic and portfolio demonstration

---

## 🛠️ Technologies Used

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Frontend

* React
* Vite
* CSS

### Tools

* Git
* GitHub
* VS Code

---

## 🗂️ Repository Contents

```text
Heart-Disease-Prediction-using-Machine-Learning-with-Python/
│
├── backend/
│   ├── main.py
│   ├── train_model.py
│   ├── requirements.txt
│   └── models/
│       └── heart_model.pkl
│
├── frontend/
│   ├── package.json
│   ├── index.html
│   └── src/
│       ├── App.jsx
│       ├── main.jsx
│       └── styles.css
│
├── data/
│   └── heart_disease_data.csv
│
├── README.md
└── .gitignore
```

---

## 📌 Dataset Description

This project uses a heart disease dataset containing patient clinical features.

| Feature    | Description                           |
| ---------- | ------------------------------------- |
| `age`      | Age of the patient                    |
| `sex`      | Gender of the patient                 |
| `cp`       | Chest pain type                       |
| `trestbps` | Resting blood pressure                |
| `chol`     | Serum cholesterol level               |
| `fbs`      | Fasting blood sugar                   |
| `restecg`  | Resting electrocardiographic result   |
| `thalach`  | Maximum heart rate achieved           |
| `exang`    | Exercise-induced angina               |
| `oldpeak`  | ST depression induced by exercise     |
| `slope`    | Slope of the peak exercise ST segment |
| `ca`       | Number of major vessels               |
| `thal`     | Thalassemia value                     |
| `target`   | Heart disease result                  |

### Target Output

| Value | Meaning                                        |
| ----- | ---------------------------------------------- |
| `0`   | Low risk / No heart disease detected           |
| `1`   | High risk / Heart disease possibility detected |

---

## ⚙️ Backend Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Manuthi24/Heart-Disease-Prediction-using-Machine-Learning-with-Python.git
cd Heart-Disease-Prediction-using-Machine-Learning-with-Python
```

### 2. Navigate to the backend folder

```bash
cd backend
```

### 3. Create a virtual environment

```bash
py -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

For Git Bash:

```bash
source venv/Scripts/activate
```

### 5. Install backend dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 6. Train the model

Before training, make sure the dataset is available in this location:

```text
data/heart_disease_data.csv
```

Then run:

```bash
python train_model.py
```

After training, the trained model will be saved inside the `models/` folder.

### 7. Run the FastAPI backend

```bash
python -m uvicorn main:app --reload
```

Backend will run on:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 💻 Frontend Installation and Setup

Open a new terminal and go to the frontend folder:

```bash
cd frontend
```

Install frontend dependencies:

```bash
npm install
```

Run the React frontend:

```bash
npm run dev
```

Frontend will run on:

```text
http://localhost:5173
```

---

## 🔗 API Endpoints

| Method | Endpoint   | Description                |
| ------ | ---------- | -------------------------- |
| `GET`  | `/`        | Check backend status       |
| `GET`  | `/health`  | Check model loading status |
| `POST` | `/predict` | Predict heart disease risk |

---

## 🧪 Sample Prediction Request

```json
{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 125,
  "chol": 212,
  "fbs": 0,
  "restecg": 1,
  "thalach": 168,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 2,
  "thal": 3
}
```

---

## 📌 Sample Prediction Response

```json
{
  "prediction": 1,
  "result": "High Risk",
  "probability": 86.45,
  "message": "The model predicts a possibility of heart disease."
}
```


### Prediction Result

```markdown
![Prediction Result](assets/screenshots/prediction-result.png)
```

---

## 🧠 Machine Learning Workflow

The machine learning workflow includes:

1. Loading the heart disease dataset
2. Performing basic data analysis
3. Preparing input features and target variable
4. Splitting data into training and testing sets
5. Training the classification model
6. Evaluating model performance
7. Saving the trained model using Joblib
8. Loading the model in the FastAPI backend
9. Sending user input from React frontend to backend
10. Returning the prediction result to the user interface

---

## 🎯 Learning Outcomes

Through this project, I improved my knowledge in:

* Exploratory Data Analysis
* Data preprocessing
* Supervised machine learning
* Classification model training
* Model evaluation
* Saving and loading ML models
* Backend API development using FastAPI
* Frontend development using React
* Connecting a machine learning model with a web application
* Building an end-to-end full-stack machine learning project

---

## 🚀 Future Improvements

* Improve model accuracy using advanced algorithms
* Add model comparison section
* Add prediction history
* Add user authentication
* Add data visualization dashboard
* Deploy backend and frontend online
* Add health tips based on risk level
* Improve UI with charts and animations

---

## 🧾 Recommended `.gitignore`

Before pushing to GitHub, make sure these files and folders are ignored:

```gitignore
venv/
backend/venv/
frontend/node_modules/
__pycache__/
*.pyc
.env
.DS_Store
```

---

## ⚠️ Medical Disclaimer

This application is developed only for educational, learning, and portfolio demonstration purposes.

The prediction result is generated by a machine learning model and may not always be accurate. It should not be considered a medical diagnosis. Always consult a qualified healthcare professional for real medical advice, diagnosis, or treatment.

---

## 👩‍💻 Author

**Manuthi24**
Data Science Undergraduate

GitHub: https://github.com/Manuthi24

---

## ⭐ Support

If you like this project, feel free to star this repository on GitHub.

![Made With Love](https://img.shields.io/badge/Made%20with-❤️-red)
![Project Type](https://img.shields.io/badge/Project--Type-Machine%20Learning-blueviolet)
![Status](https://img.shields.io/badge/Status-Completed-success)
