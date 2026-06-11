"""Train the Heart Disease Prediction model.

Run from the backend folder:
    python train_model.py

The script automatically looks for the dataset in:
    ../data/heart_disease_data.csv
    ../data/heart.csv
    data/heart_disease_data.csv
    data/heart.csv
"""

from pathlib import Path
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

FEATURE_COLUMNS = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]
TARGET_COLUMN = "target"

DATASET_CANDIDATES = [
    Path("../data/heart_disease_data.csv"),
    Path("../data/heart.csv"),
    Path("data/heart_disease_data.csv"),
    Path("data/heart.csv"),
]

MODEL_DIR = Path("models")
MODEL_PATH = MODEL_DIR / "heart_model.pkl"


def find_dataset() -> Path:
    for dataset_path in DATASET_CANDIDATES:
        if dataset_path.exists():
            return dataset_path
    raise FileNotFoundError(
        "Dataset not found. Please keep your CSV file as data/heart_disease_data.csv "
        "or data/heart.csv in the project root."
    )


def main() -> None:
    dataset_path = find_dataset()
    print(f"Using dataset: {dataset_path}")

    df = pd.read_csv(dataset_path)

    missing_columns = [col for col in FEATURE_COLUMNS + [TARGET_COLUMN] if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns in dataset: {missing_columns}")

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y if y.nunique() == 2 else None,
    )

    model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print("Training completed successfully!")
    print(f"Model saved to: {MODEL_PATH}")
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    main()
