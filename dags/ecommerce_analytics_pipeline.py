from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# --------------------
# Default arguments
# --------------------
default_args = {
    "owner": "airflow",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

# --------------------
# Task functions
# --------------------
def extract_data():
    print("Extract step completed")

def validate_raw_data():
    print("Raw data validation passed")

def transform_data():
    print("Transform step completed")

def validate_transformed_data():
    print("Transformed data validation passed")

def load_data():
    print("Load step completed")

# --------------------
# DAG definition
# --------------------
with DAG(
    dag_id="ecommerce_analytics_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
    description="E-commerce ETL pipeline with validation",
) as dag:

    extract = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data,
    )

    validate_raw = PythonOperator(
        task_id="validate_raw_data",
        python_callable=validate_raw_data,
    )

    transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data,
    )

    validate_transformed = PythonOperator(
        task_id="validate_transformed_data",
        python_callable=validate_transformed_data,
    )

    load = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

    # --------------------
    # Task dependencies
    # --------------------
    extract >> validate_raw >> transform >> validate_transformed >> load
