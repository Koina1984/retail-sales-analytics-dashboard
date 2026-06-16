import pandas as pd

df = pd.read_csv("data/raw/retail_sales.csv")

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

df["Profit_Margin"] = (df["Profit"] / df["Revenue"]) * 100

df.to_csv(
    "data/processed/cleaned_sales.csv",
    index=False
)

print("ETL Completed")
print(df.shape)