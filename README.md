# ☀️ Solar PV Annual Energy Estimation

A machine learning project designed to forecast annual solar photovoltaic (PV) energy production (kWh) based on system characteristics, geography, and timing.

## 🔗 Live Application & Assets
* **Live Streamlit Web App:** https://solar-energy-appuction-forecasting-gscfrapb8rdgbxgr2okzar.streamlit.app/
* **Trained Model Artifact:** `solar_model.pkl`
* **BI Dashboard Assets:** Included in root directory for instant Power BI deployment.

---

## 🎯 Project Objectives
* **Predictive Modeling:** Estimate annual solar energy output (kWh) using robust regression techniques.
* **Feature Engineering:** Extract critical temporal components and complex DC/AC capacity ratios.
* **Production Deployment:** Deliver an interactive Streamlit UI for real-time inference execution.
* **BI Integration:** Generate structured data exports tailored for executive Power BI dashboards.

---

## 📊 Dataset & Feature Architecture
* **Original Dataset:** 218,115 records with 17 raw features.
* **Model-Ready Dataset:** 133,535 rows after rigorous cleaning, featuring 11 dense inputs (System size in kWdc/kWac, DC-to-AC ratio, storage indicators, interconnection dates, and regional/utility categorical encoders).

---

## 🤖 Model Performance Comparison

| Model | R² Score | MAE (kWh) | RMSE (kWh) | MAPE (%) |
| :--- | :---: | :---: | :---: | :---: |
| **Random Forest Regressor (Selected)** | **0.9998** | **187.37** | **3,945.44** | **0.08%** |
| Gradient Boosting Regressor | 1.0000 | 17.60 | 367.70 | 0.03% |
| Decision Tree Regressor | 0.9977 | 635.80 | 14,564.50 | 0.18% |
| Linear Regression | -6.2900 | 26,543.30 | 819,415.00 | 40.69% |
| Ridge Regression | -19.9900 | 59,125.70 | 1,390,536.40 | 42.56% |

> *Strategic Note:* While Gradient Boosting scored structurally perfect, the tuned **Random Forest Regressor** was chosen and serialized for its robust variance handling and generalizability on unseen data, yielding a 5-fold cross-validated R² of 0.9996.

---

## 📁 Repository Structure & Key Artifacts

```text
solar-energy-production-forecasting/
├── app.py                      # Streamlit web application code
├── requirements.txt            # Python environment tracking libraries
├── solar_model.pkl             # Serialized Random Forest model & encoders
├── solar_dashboard_data.csv    # Actual vs. predicted values and error margins
├── solar_feature_importance.csv# MDI percentage scores for Power BI charts
└── solar_model_summary.csv     # High-level validation performance logs
```

### Core Files Overview:
1. **`app.py`**: Handles user input layout configurations, dropdown encoding pipelines, and dynamic real-time prediction rendering.
2. **`solar_model.pkl`**: Packaged `RandomForestRegressor` ensemble weights paired with the categorical mapping dictionary (`le_dict`).
3. **`solar_dashboard_data.csv`**: Cleansed database merged with predictions and target error arrays (`Error_kWh`) for BI visualization.

---

## 🔎 Feature Insights (MDI Importance)
1. **Estimated PV System Size (kWdc):** ~45% weight influence
2. **PV System Size (kWac):** ~41% weight influence
3. **DC-to-AC Ratio:** ~12% weight influence
4. **Metering Method & Utility:** ~2% combined weight influence

---

## 🛠️ Local Installation & Setup

To execute this forecasting engine locally on your environment:

```bash
git clone https://github.com/tiwariswati186-alt/solar-energy-production-forecasting.git
cd solar-energy-production-forecasting
pip install -r requirements.txt
streamlit run app.py
```

---

## 📈 Power BI Analytics Reporting
* Import the pre-structured `solar_dashboard_data.csv` into Power BI Desktop.
* Utilize `solar_feature_importance.csv` and `solar_model_summary.csv` to map model validation baselines and feature importance metrics for non-technical leadership review.

**Tech Stack:** Python, Streamlit, Scikit-Learn, Power BI, Pandas, NumPy, Joblib.

