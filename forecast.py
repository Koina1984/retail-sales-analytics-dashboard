import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_sales.csv")

# Monthly Revenue
monthly_sales = (
    df.groupby("Month")["Revenue"]
    .sum()
    .reset_index()
)

X = monthly_sales[["Month"]]
y = monthly_sales["Revenue"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Predict Next 3 Months
future = pd.DataFrame({
    "Month": [13, 14, 15]
})

future["Predicted_Revenue"] = model.predict(future)

print(future)

# Save Prediction
future.to_csv(
    "data/processed/forecast.csv",
    index=False
)

print("\nForecast saved successfully!")