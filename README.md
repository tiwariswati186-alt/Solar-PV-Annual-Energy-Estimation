# ☀️ Solar PV Annual Energy Estimation

A machine learning project designed to forecast annual solar photovoltaic (PV) energy production (kWh) based on system characteristics, geography, and timing.

## 🔗 Live Application & Assets
* **Live Streamlit Web App:** [Access Predictor](https://share.streamlit.io/)
* **Trained Model:** `solar_model.pkl`
* **BI Dashboard Assets:** Included in root directory for Power BI import.

---

## 🎯 Project Objectives
- **Predictive Modeling:** Estimate annual solar energy output (kWh) using regression models.
- **Feature Engineering:** Extract temporal components and DC/AC capacity ratios.
- **Production Deployment:** Interactive Streamlit UI for real-time estimates.
- **BI Integration:** Structured data exports for Power BI reporting.

---

## 📊 Dataset & Feature Architecture
* **Original Dataset:** 218,115 records and 17 raw features.
* **Model-Ready Dataset:** 133,535 records and 11 dense features (System size in kWdc/kWac, DC-to-AC ratio, storage indicator, interconnection dates, and regional/utility categorical encoders).

---

## 🤖 Model Performance Comparison

| Model | R² Score | MAE (kWh) | RMSE (kWh) | MAPE (%) |
| :--- | :---: | :---: | :---: | :---: |
| **Gradient Boosting Regressor** | **1.0000** | **17.60** | **367.70** | **0.03%** |
| **Random Forest Regressor** | **0.9998** | **187.37** | **3,945.44** | **0.08%** |
| Decision Tree Regressor | 0.9977 | 635.80 | 14,564.50 | 0.18% |
| Linear Regression | -6.2900 | 26,543.30 | 819,415.00 | 40.69% |
| Ridge Regression | -19.9900 | 59,125.70 | 1,390,536.40 | 42.56% |

> *Note:* The tuned **Random Forest Regressor** was serialized for structural robustness, yielding a Test R² of 0.9998 and a MAPE of 0.08%.

---

## 📁 Repository Structure & Key Artifacts
```text
solar-energy-production-forecasting/
├── app.py                      # Streamlit web application code
├── requirements.txt            # Python dependencies
├── solar_model.pkl             # Serialized Random Forest model & encoders
├── solar_dashboard_data.csv    # Actual vs. predicted values and error margins
├── solar_feature_importance.csv# MDI percentage scores for Power BI ranking charts
└── solar_model_summary.csv     # High-level validation metrics
```

### Core Files Overview:
1. **`app.py`**: UI logic, dropdown pipelines, dynamic model weight loading, and prediction formatting.
2. **`solar_model.pkl`**: Trained `RandomForestRegressor` and categorical mappings dictionary (`le_dict`).
3. **`solar_dashboard_data.csv`**: Combined baseline data with predictions, error arrays (`Error_kWh`), and row accuracy percentages.

---

## 🔎 Feature Insights (MDI Importance)
1. **Estimated PV System Size (kWdc):** ~45% weight
2. **PV System Size (kWac):** ~41% weight
3. **DC-to-AC Ratio:** ~12% weight
4. **Metering Method & Utility:** ~2% combined weight

---

## 🛠️ Local Installation & Setup
```bash
git clone https://github.com/tiwariswati186-alt/solar-energy-production-forecasting.git
cd solar-energy-production-forecasting
pip install -r requirements.txt
streamlit run app.py
```

---

## 📈 Power BI Reporting
* Import `solar_dashboard_data.csv` into Power BI Desktop.
* Use `solar_feature_importance.csv` and `solar_model_summary.csv` for feature impact and validation metric visualization.

**Tech Stack:** Python, Streamlit, Scikit-Learn, Pandas, NumPy, Joblib, Gdown, Power BI.
