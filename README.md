## Airflow ETL Pipeline

This project demonstrates an end-to-end ETL pipeline using Apache Airflow.

### DAG: ecommerce_analytics_pipeline
Steps:
1. extract_data
2. validate_raw_data
3. transform_data
4. validate_transformed_data
5. load_data

### Validation
Validation steps are implemented using Great Expectations (mocked for demo).

### Execution
The DAG runs successfully with all tasks completing without errors.