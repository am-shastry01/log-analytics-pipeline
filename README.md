Log Analytics Data Pipeline
Overview
The Log Analytics Data Pipeline processes large server log datasets to generate insights about API usage and system performance. The pipeline extracts log data, performs data transformation and aggregation using PySpark, stores processed metrics in PostgreSQL, and exposes analytics through a Node.js REST API.
The project demonstrates the implementation of a data engineering workflow including data processing, storage, and API-based analytics access. The entire system is containerized using Docker for reproducible deployment.
System Architecture

flowchart TD
A[Raw Server Logs Dataset] --> B[PySpark Data Processing]
B --> C[Aggregated Metrics CSV]
C --> D[PostgreSQL Database]
D --> E[Node.js REST API]
E --> F[Analytics Consumers]


Pipeline Flow:

Raw Server Logs
        ↓
PySpark ETL Processing
        ↓
Aggregated Metrics
        ↓
PostgreSQL Database
        ↓
Node.js REST API
        ↓
Analytics Consumers / Applications

Tech Stack
Programming Languages
Python
JavaScript
Data Processing
PySpark
Pandas
Database
PostgreSQL
Backend
Node.js
Express.js

Features
Processes 100,000+ server log records
Performs distributed data processing using PySpark
Calculates API endpoint usage statistics
Computes average response time per endpoint
Tracks error frequency across endpoints
Stores analytics data in PostgreSQL
Exposes processed metrics via REST API
Fully containerized pipeline using Docker
Project Structure

log-analytics-pipeline
│
├── data
│   ├── logs.csv
│   ├── endpoint_stats
│   │   └── endpoint_stats.csv
│   └── error_stats
│       └── error_stats.csv
│
├── etl
│   ├── generate_logs.py
│   └── pyspark_processing.ipynb
│
├── backend
│   ├── server.js
│   ├── package.json
│   └── Dockerfile
│
├── load_to_db.py
├── docker-compose.yml
└── README.md

Data Processing Workflow

The ETL pipeline performs the following steps:

Reads raw server logs dataset using PySpark

Extracts relevant fields such as:
API endpoint
response time
status code

Computes aggregated metrics including:
total API requests per endpoint
average response time
error count per endpoint
Stores processed metrics in CSV files
Loads aggregated results into PostgreSQL tables

Database Schema
Endpoint Statistics
Column
Type
endpoint
VARCHAR
total_requests
INTEGER
avg_response_time
FLOAT

Error Statistics
Column
Type
endpoint
VARCHAR
error_count
INTEGER

API Endpoints
Get Endpoint Usage Statistics

GET /endpoints
Example Response:
JSON
[
 {
   "endpoint": "/login",
   "total_requests": 1450,
   "avg_response_time": 210
 }
]
Get Error Statistics

GET /errors
Example Response:
JSON
[
 {
   "endpoint": "/checkout",
   "error_count": 34
 }
]
Running the Project
1 Clone the Repository
Bash
git clone https://github.com/yourusername/log-analytics-pipeline.git
cd log-analytics-pipeline
2 Start Docker Containers
Bash
docker-compose up --build
This command starts:
PostgreSQL database container
Node.js backend API container
3 Load Processed Data into PostgreSQL
Bash
python load_to_db.py
This script inserts aggregated analytics data into the database.
4 Test the API
Open in browser:

http://localhost:5000/endpoints

http://localhost:5000/errors
Example Analytics Output
The API provides insights such as:
Most frequently used API endpoints
Average response times
Error frequency per endpoint
These metrics can help analyze system performance and API usage patterns.
Key Learnings
This project demonstrates:
Building data pipelines for analytics workflows
Using PySpark for large-scale data processing
Designing PostgreSQL schemas for analytics data
Developing REST APIs with Node.js
Containerizing applications using Docker
Future Improvements
Real-time log processing using streaming frameworks
Visualization dashboard using React
Deployment to cloud infrastructure
Automated ETL scheduling