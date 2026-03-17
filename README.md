Log Analytics Data Pipeline

Overview

The Log Analytics Data Pipeline processes large server log datasets to generate insights about API usage and system performance. The pipeline extracts log data, performs data transformation and aggregation using PySpark, stores processed metrics in PostgreSQL, and exposes analytics through a Node.js REST API.

This project demonstrates a complete data engineering workflow including data processing, storage, and API-based analytics access. The system is containerized using Docker to ensure consistent deployment and reproducibility across environments.

---

System Architecture

Raw Server Logs Dataset
        ↓
PySpark Data Processing
        ↓
Aggregated Metrics (CSV)
        ↓
PostgreSQL Database
        ↓
Node.js REST API
        ↓
Analytics Consumers / Applications

---

Tech Stack

Programming Languages

- Python
- JavaScript

Data Processing

- PySpark
- Pandas

Database

- PostgreSQL

Backend

- Node.js
- Express.js

DevOps

- Docker

---

Features

- Processes 100,000+ server log records
- Performs data transformation using PySpark
- Calculates API endpoint usage statistics
- Computes average response time per endpoint
- Tracks error frequency across endpoints
- Stores analytics data in PostgreSQL
- Provides analytics through REST API endpoints
- Fully containerized pipeline using Docker

---

Project Structure

log-analytics-pipeline

data
 ├─ logs.csv
 ├─ endpoint_stats
 │   └─ endpoint_stats.csv
 └─ error_stats
     └─ error_stats.csv

etl
 ├─ generate_logs.py
 └─ pyspark_processing.ipynb

backend
 ├─ server.js
 ├─ package.json
 └─ Dockerfile

load_to_db.py
docker-compose.yml
README.md

---

Data Processing Workflow

The ETL pipeline performs the following steps:

1. Reads raw server log dataset using PySpark
2. Extracts key fields such as API endpoint, response time, and status code
3. Computes aggregated metrics including:
   - total requests per endpoint
   - average response time
   - error counts per endpoint
4. Writes processed results into CSV files
5. Loads aggregated metrics into PostgreSQL tables

---

Database Schema

Endpoint Statistics Table

Column| Type
endpoint| VARCHAR
total_requests| INTEGER
avg_response_time| FLOAT

Error Statistics Table

Column| Type
endpoint| VARCHAR
error_count| INTEGER

---

API Endpoints

Get Endpoint Usage Statistics

GET /endpoints

Example Response:

[
 {
   "endpoint": "/login",
   "total_requests": 1450,
   "avg_response_time": 210
 }
]

---

Get Error Statistics

GET /errors

Example Response:

[
 {
   "endpoint": "/checkout",
   "error_count": 34
 }
]

---

Running the Project

1. Clone the Repository

git clone https://github.com/yourusername/log-analytics-pipeline.git
cd log-analytics-pipeline

2. Start Docker Containers

docker-compose up --build

This command starts the PostgreSQL database container and the Node.js API container.

3. Load Processed Data into PostgreSQL

python load_to_db.py

This script inserts aggregated analytics data into the PostgreSQL database.

4. Test the API

Open in browser:

http://localhost:5000/endpoints

http://localhost:5000/errors

---

Example Analytics Insights

The API provides useful metrics such as:

- Most frequently used API endpoints
- Average response times
- Error frequency per endpoint

These insights help analyze system performance and identify problematic endpoints.

---

Key Learnings

This project demonstrates practical experience with:

- Designing data pipelines for analytics workflows
- Processing large datasets using PySpark
- Building REST APIs using Node.js
- Integrating PostgreSQL with backend services
- Containerizing applications using Docker

---

Future Improvements

- Real-time log processing using streaming frameworks
- Visualization dashboard using React
- Deployment on cloud infrastructure
- Automated ETL scheduling using workflow tools

---

Author

Aryan Mishra Shastry
MCA Student – Data Engineering and Backend Development