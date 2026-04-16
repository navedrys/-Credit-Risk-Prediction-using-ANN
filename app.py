# streamlit_app.py

import streamlit as st
import numpy as np
import pickle
from tensorflow import keras

# Load model and scaler
model = keras.models.load_model("model.keras")
scaler = pickle.load(open("scaler.pkl", "rb"))

# -------------------------------
# SIDEBAR (Your Credentials)
# -------------------------------
st.sidebar.title("👨‍💻 Developer Info")

st.sidebar.write("**Name:** Naved Shaikh")
st.sidebar.write("📧 Email: navedrys@gmail.com")
st.sidebar.write("📱 Phone: 7414991107")
st.sidebar.write("🔗 LinkedIn: https://linkedin.com/in/your-link")
st.sidebar.write("💻 GitHub: https://github.com/your-link")


st.title("💳 Credit Risk Prediction")

st.write("Enter customer details:")

# Example input fields (keep simple)
duration = st.number_input("Duration (months)", min_value=1)
amount = st.number_input("Loan Amount", min_value=0)
age = st.number_input("Age", min_value=18)

# Button
if st.button("Predict"):

    # Create input array (adjust features as per your model)
    input_data = np.array([[duration, amount, age]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)
    result = (prediction > 0.5).astype(int)

    # Output
    if result[0][0] == 1:
        st.success("✅ Low Risk (Loan Approved)")
    else:
        st.error("❌ High Risk (Loan Rejected)")
