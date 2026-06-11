import { useState } from 'react';

const API_URL = 'http://localhost:8000/predict';

const initialForm = {
  age: 50,
  sex: 1,
  cp: 0,
  trestbps: 120,
  chol: 200,
  fbs: 0,
  restecg: 1,
  thalach: 150,
  exang: 0,
  oldpeak: 1.0,
  slope: 1,
  ca: 0,
  thal: 2,
};

const fields = [
  { name: 'age', label: 'Age', type: 'number', min: 1, max: 120 },
  {
    name: 'sex',
    label: 'Sex',
    type: 'select',
    options: [
      { value: 0, text: 'Female' },
      { value: 1, text: 'Male' },
    ],
  },
  {
    name: 'cp',
    label: 'Chest Pain Type',
    type: 'select',
    options: [
      { value: 0, text: '0 - Typical angina' },
      { value: 1, text: '1 - Atypical angina' },
      { value: 2, text: '2 - Non-anginal pain' },
      { value: 3, text: '3 - Asymptomatic' },
    ],
  },
  { name: 'trestbps', label: 'Resting Blood Pressure', type: 'number', min: 80, max: 220 },
  { name: 'chol', label: 'Cholesterol', type: 'number', min: 100, max: 700 },
  {
    name: 'fbs',
    label: 'Fasting Blood Sugar > 120 mg/dl',
    type: 'select',
    options: [
      { value: 0, text: 'No' },
      { value: 1, text: 'Yes' },
    ],
  },
  {
    name: 'restecg',
    label: 'Resting ECG Result',
    type: 'select',
    options: [
      { value: 0, text: '0 - Normal' },
      { value: 1, text: '1 - ST-T abnormality' },
      { value: 2, text: '2 - Left ventricular hypertrophy' },
    ],
  },
  { name: 'thalach', label: 'Max Heart Rate Achieved', type: 'number', min: 60, max: 230 },
  {
    name: 'exang',
    label: 'Exercise Induced Angina',
    type: 'select',
    options: [
      { value: 0, text: 'No' },
      { value: 1, text: 'Yes' },
    ],
  },
  { name: 'oldpeak', label: 'ST Depression', type: 'number', min: 0, max: 10, step: 0.1 },
  {
    name: 'slope',
    label: 'ST Slope',
    type: 'select',
    options: [
      { value: 0, text: '0 - Upsloping' },
      { value: 1, text: '1 - Flat' },
      { value: 2, text: '2 - Downsloping' },
    ],
  },
  { name: 'ca', label: 'Major Vessels Colored', type: 'number', min: 0, max: 4 },
  {
    name: 'thal',
    label: 'Thalassemia',
    type: 'select',
    options: [
      { value: 0, text: '0' },
      { value: 1, text: '1 - Normal' },
      { value: 2, text: '2 - Fixed defect' },
      { value: 3, text: '3 - Reversible defect' },
    ],
  },
];

function App() {
  const [form, setForm] = useState(initialForm);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (event) => {
    const { name, value } = event.target;
    setForm((previous) => ({
      ...previous,
      [name]: name === 'oldpeak' ? Number.parseFloat(value) : Number.parseInt(value, 10),
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Prediction failed. Please check backend server.');
      }

      setResult(data);
    } catch (err) {
      setError(err.message || 'Something went wrong.');
    } finally {
      setLoading(false);
    }
  };

  const riskClass = result?.risk_level ? result.risk_level.toLowerCase() : '';

  return (
    <main className="page">
      <section className="hero">
        <div>
          <span className="badge">Machine Learning Healthcare App</span>
          <h1>Heart Disease Prediction System</h1>
          <p>
            Enter clinical values and get a simple heart disease risk prediction using a trained
            machine learning model.
          </p>
        </div>
        <div className="hero-card">
          <p className="hero-label">Model Output</p>
          <h2>{result ? `${result.probability_percent}%` : '--'}</h2>
          <span>{result ? `${result.risk_level} Risk` : 'Waiting for prediction'}</span>
        </div>
      </section>

      <section className="content-grid">
        <form className="form-card" onSubmit={handleSubmit}>
          <div className="form-header">
            <h2>Patient Details</h2>
            <p>Fill all fields and click predict.</p>
          </div>

          <div className="form-grid">
            {fields.map((field) => (
              <label key={field.name} className="field">
                <span>{field.label}</span>
                {field.type === 'select' ? (
                  <select name={field.name} value={form[field.name]} onChange={handleChange}>
                    {field.options.map((option) => (
                      <option key={option.value} value={option.value}>
                        {option.text}
                      </option>
                    ))}
                  </select>
                ) : (
                  <input
                    name={field.name}
                    type="number"
                    min={field.min}
                    max={field.max}
                    step={field.step || 1}
                    value={form[field.name]}
                    onChange={handleChange}
                  />
                )}
              </label>
            ))}
          </div>

          <button className="predict-btn" type="submit" disabled={loading}>
            {loading ? 'Predicting...' : 'Predict Heart Disease Risk'}
          </button>
        </form>

        <aside className="result-card">
          <h2>Prediction Result</h2>

          {error && <div className="error-box">{error}</div>}

          {!result && !error && (
            <div className="empty-state">
              <div className="pulse">❤</div>
              <p>Your prediction result will appear here.</p>
            </div>
          )}

          {result && (
            <div className={`prediction ${riskClass}`}>
              <span className="risk-pill">{result.risk_level} Risk</span>
              <h3>{result.result}</h3>
              <p className="probability">
                Probability: <strong>{result.probability_percent}%</strong>
              </p>
              <p className="note">{result.note}</p>
            </div>
          )}

          <div className="info-box">
            <h3>Feature Guide</h3>
            <p><strong>cp</strong> = chest pain type</p>
            <p><strong>trestbps</strong> = resting blood pressure</p>
            <p><strong>chol</strong> = cholesterol level</p>
            <p><strong>thalach</strong> = maximum heart rate</p>
            <p><strong>oldpeak</strong> = ST depression value</p>
          </div>
        </aside>
      </section>
    </main>
  );
}

export default App;
