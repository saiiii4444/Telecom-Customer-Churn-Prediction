telecom_churn_prediction/
│
├── data/
│   ├── raw/                # Raw dataset downloaded from the script
│   ├── processed/          # Cleaned & encoded data
│   └── download_raw_data.py
│
├── src/
│   ├── data_ingestion.py   # Cleans the raw data
│   ├── features.py         # Encodes categorical + feature engineering
│   ├── modelling.py        # ML model training & classification report
│   └── dashboard.py        # Plotly dashboard (HTML output)
│
├── notebooks/
│   └── eda_and_modelling.ipynb
│
├── dashboards/
│   └── churn_dashboard.html
│
├── docs/
│   └── overview.md
│
├── README.md
├── requirements.txt
└── pyproject.toml
