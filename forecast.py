import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv("data/processed/cleaned_sales.csv")

monthly_sales = (
    df.groupby("Month")["Revenue"]
    .sum()
    .reset_index()
)

X = monthly_sales[["Month"]]
y = monthly_sales["Revenue"]

model = LinearRegression()
model.fit(X, y)

future_months = np.array([[13], [14], [15]])

predictions = model.predict(future_months)

print("Forecast:")
for i, pred in enumerate(predictions, start=13):
    print(f"Month {i}: {pred:.2f}")