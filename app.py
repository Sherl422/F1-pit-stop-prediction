# app.py

import streamlit as st
import pandas as pd
import pickle

# Load model
with open("f1pitstops.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏎️ F1 Pit Stop Prediction")

st.write("Predict probability of a pit stop in the next lap.")

# Inputs
TyreLife = st.number_input("Tyre Life", min_value=0)

Cumulative_Degradation = st.number_input(
    "Cumulative Degradation",
    min_value=0.0,
    format="%.2f"
)

LapTime_Delta = st.number_input(
    "Lap Time Delta",
    format="%.2f"
)

LapNumber = st.number_input("Lap Number", min_value=1)

Stint = st.number_input("Stint", min_value=1)

RaceProgress = st.slider(
    "Race Progress (%)",
    min_value=0.0,
    max_value=100.0,
    format="%.2f"
)

Position = st.number_input("Current Position", min_value=1)

Position_Change = st.number_input("Position Change")

Compound = st.selectbox(
    "Tyre Compound",
    ["HARD", "MEDIUM", "SOFT", "INTERMEDIATE", "WET"]
)

# Create input dataframe
input_data = pd.DataFrame({
    "TyreLife": [TyreLife],
    "Cumulative_Degradation": [Cumulative_Degradation],
    "LapTime_Delta": [LapTime_Delta],
    "LapNumber": [LapNumber],
    "Stint": [Stint],
    "RaceProgress": [RaceProgress],
    "Position": [Position],
    "Position_Change": [Position_Change],
    "Compound": [Compound]
})

# One-hot encoding
input_data = pd.get_dummies(input_data, drop_first=True)

# Match training columns
expected_columns = [
    'TyreLife',
    'Cumulative_Degradation',
    'LapTime_Delta',
    'LapNumber',
    'Stint',
    'RaceProgress',
    'Position',
    'Position_Change',
    'Compound_INTERMEDIATE',
    'Compound_MEDIUM',
    'Compound_SOFT',
    'Compound_WET'
]

for col in expected_columns:
    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[expected_columns]

# Prediction
if st.button("Predict"):
    prediction = model.predict_proba(input_data)[0][1]

    st.subheader("Pit Stop Probability")
    st.write(f"{prediction:.2%}")

    if prediction > 0.7:
        st.error("High chance of pit stop next lap")
    elif prediction > 0.4:
        st.warning("Moderate chance of pit stop")
    else:
        st.success("Low chance of pit stop")