import pandas as pd
import random
from datetime import datetime, timedelta

endpoints = [
    "/login",
    "/products",
    "/orders",
    "/cart",
    "/checkout",
    "/profile",
]

status_code = [200, 200, 200, 200, 404, 500]

data = []

start = datetime.now()

for i in range(100000):
    data.append({
        "timestamp": start + timedelta(seconds=i),
        "endpoints": random.choice(endpoints),
        "status": random.choice(status_code),
        "response_time": random.randint(50, 500)
    })

df = pd.DataFrame(data)

df.to_csv("../data/logs.csv", index=False)
print("Dataset created 100000 logs")
