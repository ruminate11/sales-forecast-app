from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io, base64

app = Flask(__name__)

# =========================
# Load CSV only (NO MODEL)
# =========================
df = pd.read_csv("data/sales.csv")


# =========================
# Simple Forecast Function
# =========================
def get_forecast():
    # moving average of last 30 days
    return round(float(df["sales"].tail(30).mean()), 2)


# =========================
# Graph generator
# =========================
def create_sales_graph(history, forecast_val, reorder_point=None):

    plt.figure(figsize=(6, 3.5))

    x_hist = range(len(history))
    x_fore = len(history)

    # Historical line
    plt.plot(x_hist, history,
             marker="o",
             linewidth=2,
             color="blue",
             label="Historical Sales")

    # Forecast point
    plt.scatter(x_fore, forecast_val,
                s=120,
                color="green",
                label="Forecast")

    # Reorder point
    if reorder_point:
        plt.axhline(reorder_point,
                    linestyle="--",
                    linewidth=2,
                    color="red",
                    label="Reorder Point")

    plt.xlabel("Days")
    plt.ylabel("Units Sold")
    plt.title("Sales Trend + Forecast")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=120)
    buf.seek(0)

    img = base64.b64encode(buf.getvalue()).decode()
    plt.close()

    return img


# =========================
# Home
# =========================
@app.route("/")
def home():

    forecast = get_forecast()
    history = df["sales"].tail(20).values

    graph = create_sales_graph(history, forecast)

    return render_template(
        "index.html",
        forecast=forecast,
        graph=graph
    )


# =========================
# Calculate reorder point
# =========================
@app.route("/calculate", methods=["POST"])
def calculate():

    forecast = float(request.form["forecast"])
    lead_time = float(request.form["lead_time"])
    safety_stock = float(request.form["safety_stock"])

    avg_daily = forecast / 30
    reorder_point = round((lead_time * avg_daily) + safety_stock, 2)

    history = df["sales"].tail(20).values
    graph = create_sales_graph(history, forecast, reorder_point)

    return render_template(
        "index.html",
        forecast=forecast,
        reorder_point=reorder_point,
        graph=graph
    )


if __name__ == "__main__":
    app.run(debug=True)
