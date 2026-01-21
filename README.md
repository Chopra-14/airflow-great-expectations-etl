# 🛒 Airflow ETL Pipeline with Great Expectations

## 📌 Project Overview

This project implements an **end-to-end ETL pipeline** using **Apache Airflow**, **Great Expectations**, and **Docker**.  
The pipeline extracts e-commerce data, validates data quality, performs transformations, and loads the processed data while ensuring **data reliability through automated validations**.

The entire system is **containerized** and **production-aligned**, following modern data engineering best practices.

---

## 🏗 Architecture Overview

### 🔁 ETL Flow

```text
Extract Data
   ↓
Validate Raw Data (Great Expectations)
   ↓
Transform Data
   ↓
Validate Transformed Data (Great Expectations)
   ↓
Load Data
🧩 Components
Airflow Webserver & Scheduler – Workflow orchestration

ETL Service (Python) – Transformations & unit tests

Great Expectations – Data quality validation

PostgreSQL – Airflow metadata database

Docker Compose – Service orchestration

🧰 Tool Stack
Tool	Purpose
Apache Airflow	Workflow orchestration
Great Expectations	Data validation
Python 3.10	ETL logic
Docker & Docker Compose	Containerization
Pytest	Unit testing
SQLite	Analytics data storage
Git & GitHub	Version control
⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/Chopra-14/airflow-great-expectations-etl.git
cd airflow-great-expectations-etl
2️⃣ Environment Variables
Create .env.example:

AIRFLOW_UID=50000
SQLITE_DB_PATH=/data/analytics.db
3️⃣ Start All Services
docker-compose up -d
4️⃣ Verify Containers
docker ps
Ensure the following containers are running:

airflow_webserver

airflow_scheduler

etl-service

postgres

🚀 DAG Execution Steps
Open Airflow UI

http://localhost:8080
Enable the DAG
ecommerce_analytics_pipeline

Trigger the DAG manually ▶️

Confirm:

All tasks turn GREEN

DAG run status = SUCCESS

✅ DAG Configuration
Setting	Value
Schedule	@daily
Retries	2
Retry Delay	5 minutes
Catchup	False
🔍 Validation Strategy (Great Expectations)
✔ Raw Data Validation
Column presence checks

Schema consistency

Executed via Great Expectations checkpoint

✔ Transformed Data Validation
Schema integrity checks

Data consistency checks

✔ Failure Handling
DAG fails immediately if validation fails

Downstream tasks are blocked

🧪 Unit Testing
Run tests inside the ETL container:

docker-compose exec etl-service pytest
Included Tests
Transformation logic test

Schema validation test

✔ Passing tests ensure reliable ETL logic

🗂 Screenshots (Evidence)
Screenshots included in the repository:

Screenshot	Description
step13_01_docker_ps_running.png	All containers running
step14_02_airflow_dag_list.png	DAG visible in Airflow
step14_03_dag_graph_view.png	DAG graph view
step14_04_dag_grid_success.png	All tasks successful
step14_05_task_log_success.png	Task log output
step14_06_great_expectations_data_docs.png	Great Expectations Data Docs
step12_01_pytest_success.png	Pytest success
⭐ Bonus Screenshots
Great Expectations CLI validation

Expectation Suite HTML

Data Docs index page

🗄 How to Verify SQLite Database
Enter the ETL container:

docker-compose exec etl-service bash
Open SQLite database:

sqlite3 /data/analytics.db
List tables:

.tables
Preview data:

SELECT * FROM analytics_table LIMIT 5;
🏁 Final Status
✔ Fully containerized
✔ Automated validation implemented
✔ Unit test coverage added
✔ End-to-end execution verified
✔ Portfolio-ready project

🙌 Author
Chopra Lakshmi Sathvika
Data Engineering | Apache Airflow | Great Expectations | Docker

