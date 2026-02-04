# train_forecast.py

import pandas as pd
import joblib
import matplotlib.pyplot as plt

from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv("data/sales.csv", parse_dates=["date"])
df.set_index("date", inplace=True)

# -------------------
# Decomposition
# -------------------
result = seasonal_decompose(df["sales"], model="additive", period=12)
result.plot()
plt.show()

# -------------------
# SARIMA Model
# -------------------
model = SARIMAX(
    df["sales"],
    order=(1,1,1),
    seasonal_order=(1,1,1,12)
)

fit = model.fit()

# Save model
joblib.dump(fit, "forecast_model.pkl")

print("Forecast model saved as forecast_model.pkl")
