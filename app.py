import streamlit as st
import joblib
import numpy as np
import os

# Page config
st.set_page_config(page_title="AQI Prediction", layout="centered")

st.title("Air Quality Index (AQI) Prediction")
st.write("Enter pollutant values to predict AQI")

# ---- Check model file ----
MODEL_FILE = "LR_AQI_Prediction.joblib"

if not os.path.exists(MODEL_FILE):
    st.error("❌ Model file not found!")
    st.stop()

# ---- Load model ----
model = joblib.load(MODEL_FILE)

# ---- Inputs ----
pm25 = st.number_input("PM2.5", min_value=0.0, value=50.0)
pm10 = st.number_input("PM10", min_value=0.0, value=80.0)
no2 = st.number_input("NO2", min_value=0.0, value=40.0)
so2 = st.number_input("SO2", min_value=0.0, value=20.0)
co = st.number_input("CO", min_value=0.0, value=1.0)
temp = st.number_input("Temperature (°C)", value=30.0)
humidity = st.number_input("Humidity (%)", value=60.0)

# ---- Predict ----
if st.button("Predict AQI"):
    input_data = np.array([[pm25, pm10, no2, so2, co, temp, humidity]])
    prediction = model.predict(input_data)[0]

    st.success(f"🌫️ Predicted AQI: {prediction:.2f}")

    # ---- AQI Category ----
    if prediction <= 50:
        st.info("🟢 Good Air Quality")
    elif prediction <= 100:
        st.success("🟡 Moderate Air Quality")
    elif prediction <= 200:
        st.warning("🟠 Poor Air Quality")
    else:
        st.error("🔴 Very Poor / Hazardous Air Quality")
