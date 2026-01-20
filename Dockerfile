FROM apache/airflow:2.7.3

USER airflow

RUN pip install --no-cache-dir --default-timeout=100 great-expectations==0.18.21
