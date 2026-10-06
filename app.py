import streamlit as st
import numpy as np
import joblib

model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Medical Insurance Cost Prediction")

st.write(
    "Enter the age to predict medical insurance charges."
)

age = st.number_input(
    "Enter Age",
    min_value=1,
    max_value=100,
    value=35,
    step=1
)

if st.button("Predict Insurance Cost"):

    sample_age = np.array([[age]])

    sample_age_scaled = scaler.transform(sample_age)

    prediction = model.predict(sample_age_scaled)

    st.success(
        "Predicted Medical Insurance Charges: ₹"
        + str(round(float(prediction[0]), 2))
    )