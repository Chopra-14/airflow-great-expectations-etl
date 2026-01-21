# 🛒 Airflow ETL Pipeline with Great Expectations

## 📌 Project Overview

This project implements an **end-to-end ETL pipeline** using **Apache Airflow**, **Great Expectations**, and **Docker**.  
The pipeline extracts e-commerce data, validates data quality, performs transformations, and loads the processed data while ensuring **data reliability through automated validations**.

The entire system is **containerized** and follows modern **data engineering best practices**.

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

```

## 🧩 Components
```

- **Airflow Webserver & Scheduler** – Workflow orchestration  
- **ETL Service (Python)** – Data transformation logic & unit tests  
- **Great Expectations** – Data quality validation  
- **PostgreSQL** – Airflow metadata database  
- **Docker Compose** – Service orchestration  
```

## 🧰 Tool Stack
```

| Tool | Purpose |
|------|--------|
| Apache Airflow | Workflow orchestration |
| Great Expectations | Data validation |
| Python 3.10 | ETL logic |
| Docker & Docker Compose | Containerization |
| Pytest | Unit testing |
| SQLite | Analytics data storage |
| Git & GitHub | Version control |
```

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Chopra-14/airflow-great-expectations-etl.git
cd airflow-great-expectations-etl
```
### 2️⃣ Environment Variables
```
Create a file named `.env.example`:

```env
AIRFLOW_UID=50000
SQLITE_DB_PATH=/data/analytics.db
```

### 3️⃣ Start All Services
```
Start all containers using Docker Compose:

```bash
docker-compose up -d
```
### 4️⃣ Verify Containers

Check that all required containers are running:

```bash
docker ps
```
```
Ensure the following containers are running:

- `airflow_webserver`
- `airflow_scheduler`
- `etl-service`
- `postgres`
```

## 🚀 DAG Execution Steps
```
1. Open the Airflow UI  
   👉 http://localhost:8080

2. Enable the DAG:
   - `ecommerce_analytics_pipeline`

3. Trigger the DAG manually ▶️

4. Confirm:
   - All tasks turn **GREEN**
   - DAG run status = **SUCCESS**

---
```
## ✅ DAG Configuration
```
| Setting       | Value        |
|--------------|--------------|
| Schedule     | `@daily`     |
| Retries      | `2`          |
| Retry Delay  | `5 minutes`  |
| Catchup      | `False`      |
```

## 🔍 Validation Strategy (Great Expectations)

### ✔ Raw Data Validation
```
- Column presence checks
- Schema consistency
- Executed via **Great Expectations checkpoint**
```
### ✔ Transformed Data Validation
```
- Schema integrity checks
- Data consistency checks
```
### ✔ Failure Handling
```
- DAG fails immediately if validation fails
- Downstream tasks are blocked
```

## 🧪 Unit Testing

Run tests inside the ETL container:

```bash
docker-compose exec etl-service pytest
```
### Included Tests
```
- Transformation logic test
- Schema validation test

✔ Passing tests ensure reliable ETL logic
```

## 🗂 Screenshots (Evidence)

### 📁 screenshots/
```

| Screenshot | Description |
|----------|-------------|
| Screenshot_5_docker_ps_running.png | All containers running |
| Screenshot_6_pytest_success.png | Pytest success |
| Screenshot_1_Data_Docs_Validation_Result.png | Great Expectations Data Docs |
| Screenshot_2_Raw_Data_Suite_Detail.png | Raw data expectation suite |
| Screenshot_3_Checkpoint_Run_Success.png | Checkpoint run success |
| Screenshot_4_ge_checkpoint_cli.png | Great Expectations CLI checkpoint run |
```
```
📁 screenshots/dags_screenshots/
Screenshot	Description
01_airflow_dags_page.png	DAG list
02_dag_grid_success.png	DAG grid success
03_dag_graph_view.png	DAG graph view
04_dag_run_details.png	DAG run details
05_task_log_success.png	Task log output
06_dag_code_file.png	DAG code file
```

⭐ **Includes mandatory + bonus screenshots**
```
---

## 🗄 How to Verify SQLite Database

Enter the ETL container:

```bash
docker-compose exec etl-service bash
```
Open the SQLite database:

```bash
sqlite3 /data/analytics.db
```
List tables:

```sql
.tables
```
### Preview Data

```sql
SELECT * FROM analytics_table LIMIT 5;
```
```

## 🏁 Final Status
```
- ✔ Fully containerized
- ✔ Automated data validation implemented
- ✔ Unit test coverage added
- ✔ End-to-end execution verified
- ✔ Portfolio-ready project
```

## 🙌 Author
```
**Chopra Lakshmi Sathvika**  
Data Engineering | Apache Airflow | Great Expectations | Docker
```
