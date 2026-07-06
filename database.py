import pandas as pd
import sqlite3

# Read cleaned dataset
df = pd.read_csv("data/processed/cleaned_sales.csv")

# Create database
conn = sqlite3.connect("sales.db")

# Save dataframe as SQL table
df.to_sql("sales", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("Database Created Successfully!")