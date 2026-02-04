from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

model = joblib.load("forecast_model.pkl")
df = pd.read_csv("data/sales.csv")


@app.route("/")
def home():

    forecast = model.forecast(steps=2).iloc[0]
    forecast = round(float(forecast), 2)

    return render_template("index.html", forecast=forecast)


@app.route("/calculate", methods=["POST"])
def calculate():

    forecast = float(request.form["forecast"])
    lead_time = float(request.form["lead_time"])
    safety_stock = float(request.form["safety_stock"])

    avg_daily = forecast / 30

    reorder_point = (lead_time * avg_daily) + safety_stock

    return render_template(
        "index.html",
        forecast=forecast,
        reorder_point=round(reorder_point, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)
