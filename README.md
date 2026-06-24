🚀 Crypto Data Platform (Airflow + PostgreSQL + Streamlit)

A fully automated end-to-end data engineering pipeline that extracts live cryptocurrency data from an API, processes it using Airflow, stores it in a PostgreSQL data warehouse, and visualizes insights through an interactive Streamlit dashboard.

📌 Overview

This project simulates a real-world data engineering system where live market data is:

Extracted from a public crypto API
Orchestrated using Apache Airflow
Stored in a PostgreSQL warehouse
Visualized using Streamlit dashboards

It demonstrates the full lifecycle of a modern data pipeline:
Ingestion → Processing → Storage → Analytics → Visualization

🧠 Architecture
             ┌──────────────┐
             │ Crypto API   │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │  Airflow     │
             │ (Orchestrator│
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │ PostgreSQL   │
             │ Data Warehouse│
             └──────┬───────┘
        ┌───────────┴───────────┐
        ↓                       ↓
  SQL Analysis           Streamlit Dashboard
⚙️ Tech Stack
Python – Data ingestion & processing
Airflow – Workflow orchestration
PostgreSQL – Data warehouse
Requests – API integration
Pandas – Data transformation
Streamlit – Interactive dashboard
SQL – Data analysis
📊 Features
🔄 Automated Data Pipeline
Scheduled data extraction using Airflow DAGs
Handles continuous ingestion of crypto market data
🧹 Data Processing
Cleans and validates raw API responses
Ensures structured and consistent data storage
🏦 Data Warehouse
Stores historical crypto price data
Enables SQL-based analytics and querying
📈 Interactive Dashboard
Live crypto price tracking
Historical trends visualization
Easy-to-use UI built with Streamlit
🪄 Example Dashboard Features
📉 Price trends over time
💰 Current crypto prices (BTC, ETH, SOL)
📊 Average price comparison
🔍 Filter by cryptocurrency
🔄 Live refresh capability
🧱 Database Schema
crypto_prices (
    id SERIAL PRIMARY KEY,
    symbol TEXT,
    price_usd FLOAT,
    market_cap FLOAT,
    volume_24h FLOAT,
    timestamp TIMESTAMP
)
🚀 How It Works
Airflow triggers a DAG on schedule
DAG calls the crypto API
Data is cleaned and validated
Clean data is inserted into PostgreSQL
Streamlit reads data from warehouse
Dashboard visualizes insights
📦 Installation
git clone https://github.com/your-username/crypto-data-platform.git
cd crypto-data-platform
pip install -r requirements.txt
▶️ Run the Project
1. Start Airflow
airflow standalone
2. Run Streamlit Dashboard
streamlit run app.py
3. Start PostgreSQL

Make sure your database is running locally.


🧠 What I Learned
Building end-to-end ETL pipelines
Working with real-time APIs
Data orchestration using Airflow
Designing warehouse schemas
Creating analytics dashboards
Connecting backend systems to UI

📈 Future Improvements
Add Kafka for real-time streaming ingestion
Deploy on AWS (EC2 + RDS + S3)
Add dbt for transformations
Add Docker for containerization
Add authentication to dashboard
Expand to multi-source financial data
💡 Why This Project Matters

This project reflects how modern data systems are built in production environments:

Raw data → Orchestration → Warehouse → Analytics → Dashboard

It bridges the gap between learning and real-world Data Engineering.

🧑‍💻 Author

Built by a student on a Data Engineering roadmap 🚀
