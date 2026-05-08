# 🏎️ F1 Pit Stop Prediction

An end-to-end Machine Learning project that predicts the probability of a pit stop in the next lap using race telemetry and tyre data.

## 🚀 Project Overview
This project uses an XGBoost classifier to analyze Formula 1 race data and predict pit stop decisions based on tyre wear, lap progress, position changes, and race conditions.

## 📊 Features Used
- TyreLife
- Cumulative Degradation
- Lap Time Delta
- Lap Number
- Stint
- Race Progress
- Position
- Position Change
- Tyre Compound

## 🧠 Model
- Algorithm: XGBoost Classifier
- Metric: ROC-AUC Score
- Preprocessing: One-Hot Encoding for categorical variables

## 🖥️ Web App
Built using **Streamlit** for real-time predictions.

## 📦 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Streamlit


## ⚙️ How to Run Locally

```bash
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\Activate.ps1   # Windows

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
