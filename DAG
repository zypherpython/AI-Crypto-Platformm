import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


from src.extract import fetch_raw_data
from src.transform import clean_data
from src.load import load
from src.database import get_connection

with DAG(
    dag_id="crypto_pipeline",
    start_date=datetime(2026, 6, 30),
    schedule_interval="0 */6 * * *"  # every 6 hours,
    catchup=False,
) as dag:

    def run_pipeline():
        raw = fetch_raw_data()
        df = clean_data(raw)
        conn = get_connection()
        load(df, conn)
        conn.close()

    pipeline_task = PythonOperator(
        task_id="run_crypto_pipeline",
        python_callable=run_pipeline,
    )
