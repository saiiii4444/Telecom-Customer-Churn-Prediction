# 📡 Telecom Customer Churn Prediction  
Predicting customer attrition for French telecom operators using an end-to-end Machine Learning pipeline.

---

## 📌 1. Overview

The French telecom industry (Orange, SFR, Bouygues, Free) experiences some of the highest churn rates in Europe.  
Customers switch operators frequently due to:

- Price competition  
- Network coverage issues  
- Customer service dissatisfaction  
- Contract types  
- Multi-service bundles (Internet + TV + Mobile)  

This project implements a **complete churn prediction system** designed for real telecom retention teams.

---

## 🎯 2. Business Problem (France Context)

The average **telecom churn rate in France is 18%–28%**, resulting in:

- Lost recurring revenue  
- Increased acquisition costs  
- Lower customer lifetime value  
- Higher marketing expenses  

A predictive model enables operators to:

- Identify high-risk customers  
- Prevent churn early  
- Optimize retention offers  
- Reduce revenue leakage  

telecom_churn_prediction/
│
├── data/
│ ├── raw/
│ ├── processed/
│ └── download_raw_data.py
│
├── src/
│ ├── data_ingestion.py
│ ├── features.py
│ ├── modelling.py
│ └── dashboard.py
│
├── dashboards/
│ └── churn_dashboard.html
│
├── notebooks/
│ └── eda_and_modelling.ipynb
│
├── docs/
│ └── overview.md
│
├── requirements.txt
├── pyproject.toml
└── README.md


---

## 🗂 4. Dataset

Dataset used: **IBM Telco Customer Churn**  
A real-world dataset widely used in telecom retention analytics.

### Feature Groups

| Category | Features | Description |
|----------|----------|-------------|
| Demographic | gender, seniorCitizen, partner | Basic customer profile |
| Contract | tenure, contract type, paymentMethod | Customer stability |
| Services | internetService, phoneService, streaming | Bundle usage |
| Billing | monthlyCharges, totalCharges | Price sensitivity |
| Target | Churn (Yes/No) | Binary classification label |

---

## 🔧 5. Full Pipeline

### **Step 1 — Download Raw Data**
```bash
python data/download_raw_data.py

Step 2 — Data Ingestion (Cleaning)
python src/data_ingestion.py \
  --input_path data/raw/telco_churn.csv \
  --output_path data/processed/clean.csv

Step 3 — Feature Engineering (OHE)
python src/features.py \
  --input_path data/processed/clean.csv \
  --output_path data/processed/features.csv

Step 4 — Model Training
python src/modelling.py \
  --input_path data/processed/features.csv \
  --report_path data/processed/model_report.csv

Step 5 — Dashboard Export
python src/dashboard.py \
  --input_path data/processed/features.csv \
  --output_path dashboards/churn_dashboard.html

📊 6. Key KPIs Tracked

Churn Rate

High-Risk Customer %

Tenure-wise churn

Monthly charges impact

Bundle usage vs churn

Contract stability analysis

Customer profitability vs churn

🧠 7. Insights (Typical)

These insights match real French telecom market behavior:

Month-to-month customers churn the most

Tenure < 6 months = extremely high churn probability

High monthly charges → higher churn

Fiber customers churn less (long-term contracts)

Auto-pay reduces churn

Customers with multiple services (bundles) are more loyal

🤖 8. Machine Learning Model
Model:

GradientBoostingClassifier

Why:

Handles nonlinear customer behavior

Good for mixed numerical + categorical data

Works well on imbalanced datasets

Stable without heavy tuning

Expected Results:

Accuracy: 80–86%

Recall (Churn customers): 65–75%

F1 score (Churn): 68–72%

🏗 9. System Architecture (ASCII Diagram)
         ┌─────────────────────────┐
         │    Raw Telecom Data     │
         └──────────────┬──────────┘
                        ▼
             Data Ingestion (Clean)
                        │
                        ▼
            Feature Engineering (OHE)
                        │
                        ▼
                 ML Model Training
                        │
                        ▼
            Churn Probability Scores
                        │
                        ▼
            Dashboard + Business Report

🚀 10. How to Run the Entire Project
Install Dependencies
pip install -r requirements.txt

Run the Pipeline
python data/download_raw_data.py
python src/data_ingestion.py --input_path data/raw/telco_churn.csv --output_path data/processed/clean.csv
python src/features.py --input_path data/processed/clean.csv --output_path data/processed/features.csv
python src/modelling.py --input_path data/processed/features.csv --report_path data/processed/model_report.csv
python src/dashboard.py --input_path data/processed/features.csv --output_path dashboards/churn_dashboard.html

🏁 11. Conclusion

This project provides a production-grade churn prediction solution tailored to French telecom operators.

It showcases strong skills in:

Business analysis

Data engineering

Feature engineering

Machine learning

Churn modeling

Dashboarding

Telecom analytics

A high-value project for Data Analyst, Business Analyst, and Data Scientist roles in France.
---

## 🧱 3. Project Structure

