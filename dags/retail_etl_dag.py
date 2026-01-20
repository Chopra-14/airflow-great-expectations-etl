from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="retail_etl_with_great_expectations",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=["etl", "great_expectations"],
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command="echo 'Extract step completed'",
    )

    validate = BashOperator(
        task_id="validate",
        bash_command="great_expectations checkpoint run raw_data_checkpoint",
    )

    load = BashOperator(
        task_id="load",
        bash_command="echo 'Load step completed'",
    )

    extract >> validate >> load
