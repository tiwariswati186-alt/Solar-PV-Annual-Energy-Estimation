import streamlit as st
import numpy as np
import joblib  # pickle ki jagah joblib use kar rahe hain

# Page configuration aur styling
st.set_page_config(page_title="Solar Energy Predictor", page_icon="☀️", layout="centered")

st.title("☀️ Solar Energy Production Forecasting")
st.markdown("Predict the annual energy production (kWh) for solar installations.")

# Load the trained model and label encoders
@st.cache_resource
def load_model():
    with open("solar_model.pkl", "rb") as file:
        data = joblib.load(file) # joblib se load kar rahe hain
    return data

data = load_model()
model = data["model"]
le_dict = data["le_dict"]

# User Input UI (Dropdowns & Sliders)
st.header("Enter Installation Details")

col1, col2 = st.columns(2)

with col1:
    developer = st.selectbox("Developer", list(le_dict['Developer'].classes_))
    division = st.selectbox("Division", list(le_dict['Division'].classes_))
    county = st.selectbox("County", list(le_dict['County'].classes_))
    utility = st.selectbox("Utility", list(le_dict['Utility'].classes_))
    metering_method = st.selectbox("Metering Method", list(le_dict['Metering Method'].classes_))

with col2:
    pv_size_kwdc = st.slider("PV System Size (kWdc)", min_value=0.1, max_value=200.0, value=10.0, step=0.1)
    pv_size_kwac = st.slider("PV System Size (kWac)", min_value=0.1, max_value=200.0, value=8.0, step=0.1)
    has_storage_system = st.selectbox("Energy Storage System?", ["No", "Yes"])
    interconnection_year = st.number_input("Interconnection Year", min_value=2010, max_value=2030, value=2025)
    interconnection_month = st.slider("Interconnection Month", min_value=1, max_value=12, value=6)

# Prediction Logic
if st.button("🔮 Predict Annual Production"):
    
    def safe_encode(le, val):
        return list(le.classes_).index(val)
    
    storage_binary = 1 if has_storage_system == "Yes" else 0
    kwdc_to_kwac_ratio = pv_size_kwdc / (pv_size_kwac + 1e-6)
    
    features = [
        pv_size_kwdc,
        pv_size_kwac,
        kwdc_to_kwac_ratio,
        storage_binary,
        interconnection_year,
        interconnection_month,
        safe_encode(le_dict['Developer'], developer),
        safe_encode(le_dict['Division'], division),
        safe_encode(le_dict['County'], county),
        safe_encode(le_dict['Metering Method'], metering_method),
        safe_encode(le_dict['Utility'], utility)
    ]
    
    pred_log = model.predict([features])
    prediction_kwh = np.expm1(pred_log)[0]
    
    st.success(f"🔮 Estimated Annual Production: **{prediction_kwh:,.2f} kWh**")
    st.info(f"⚡ Equivalent to approx **{prediction_kwh/1000:.2f} MWh** per year.")
