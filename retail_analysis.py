import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

num_records = 25000

start_date = datetime(2025, 1, 1)

categories = [
    "Electronics",
    "Clothing",
    "Furniture",
    "Groceries",
    "Sports"
]

data = {
    "Transaction_ID": range(1, num_records + 1),
    "Customer_ID": np.random.randint(1000, 5000, num_records),
    "Category": np.random.choice(categories, num_records),
    "Units_Sold": np.random.randint(1, 10, num_records),
    "Unit_Price": np.random.randint(50, 2000, num_records),
    "Date": [
        start_date + timedelta(days=np.random.randint(0, 365))
        for _ in range(num_records)
    ]
}

df = pd.DataFrame(data)

df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

df["Cost"] = df["Revenue"] * np.random.uniform(
    0.5,
    0.9,
    len(df)
)

df["Profit"] = df["Revenue"] - df["Cost"]

df.to_csv(
    "data/raw/retail_sales.csv",
    index=False
)

print("Dataset created successfully")
print(df.head())
print("Rows:", len(df))