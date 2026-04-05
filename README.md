# 🌦️ Weather Data Pipeline (End-to-End)

This project demonstrates a fully automated data pipeline that ingests real-time weather data, processes it, and visualizes insights using modern data engineering tools.

## 🧱 Tech Stack

- Apache Airflow (Orchestration)
- AWS S3 (Data Lake)
- Snowflake (Data Warehouse)
- dbt (Transformation)
- Tableau (Dashboard)
- Python (Ingestion)

## ⚙️ Architecture

API → S3 → Snowflake → dbt → Tableau  
         ↑  
     Airflow Automation

## 🚀 Features

- Real-time weather data ingestion from API
- Automated scheduling using Airflow (every 5 minutes)
- Data stored in AWS S3
- Data loaded into Snowflake
- Data transformation using dbt
- Dashboard visualization using Tableau

## 📁 Project Structure

weather-data-pipeline/
│
├── ingestion/
│   └── weather_to_s3.py
│
├── airflow/
│   └── weather_pipeline_dag.py
│
├── dbt/
│   ├── models/
│   └── dbt_project.yml
│
├── requirements.txt
└── README.md


## 🛠️ Setup Instructions

### 1. Clone repository
```bash
git clone <https://github.com/anuragsahoo1/weather-data-pipeline.git>
cd weather-data-pipeline
