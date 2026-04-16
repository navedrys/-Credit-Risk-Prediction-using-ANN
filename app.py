import streamlit as st
import numpy as np
import pickle
from tensorflow import keras

# Load model & scaler
model = keras.models.load_model("model.keras")
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("💳 Credit Risk Prediction")

st.sidebar.title("👨‍💻 Developer")
st.sidebar.write("Naved Shaikh")
st.sidebar.write("📧 navedrys@gmail.com")
st.sidebar.write("📱 7414991107")

st.write("Enter values:")

# IMPORTANT: number of inputs must match training features
num_features = scaler.mean_.shape[0]

inputs = []
for i in range(num_features):
    val = st.number_input(f"Feature {i+1}", value=0.0)
    inputs.append(val)

if st.button("Predict"):
    data = np.array([inputs])
    data = scaler.transform(data)

    pred = model.predict(data)

    if pred[0][0] > 0.5:
        st.success("✅ Low Risk")
    else:
        st.error("❌ High Risk")
