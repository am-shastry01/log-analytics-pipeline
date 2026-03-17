import pandas as pd
import psycopg2

# read processed data
df = pd.read_csv("../data/endpoint_stats/endpoint_stats.csv")
df2 = pd.read_csv("../data/error_stats/error_stats.csv")

# connect to postgres
conn = psycopg2.connect(
    host="localhost",
    database="sales_analytics_pipline",
    user="postgres",
    password="Aryan930054"
)

cur = conn.cursor()

# insert endpoint analytics
for _, row in df.iterrows():
    cur.execute(
        "INSERT INTO endpoint_stats (endpoint, total_requests, avg_response_time) VALUES (%s, %s, %s)",
        (row['endpoints'], row['total_requests'], row['avg_response_time'])
    )

# insert error analytics
for _, row in df2.iterrows():
    cur.execute(
        "INSERT INTO error_stats (endpoint, error_count) VALUES (%s, %s)",
        (row['endpoints'], row['error_count'])
    )

conn.commit()

cur.close()
conn.close()

print("Data loaded into PostgreSQL")