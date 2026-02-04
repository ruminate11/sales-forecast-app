# generate_data.py

import numpy as np
import pandas as pd
import os

np.random.seed(42)

months = 60  # 5 years

dates = pd.date_range(start="2020-01-01", periods=months, freq="ME")

trend = np.linspace(400, 800, months)
seasonality = 150 * np.sin(np.arange(months) * 2*np.pi/12)
noise = np.random.normal(0, 40, months)

sales = trend + seasonality + noise

df = pd.DataFrame({
    "date": dates,
    "sales": sales.round()
})

os.makedirs("data", exist_ok=True)
df.to_csv("data/sales.csv", index=False)

print("Sales dataset created at data/sales.csv")
print(df.head())
