from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

prices = pd.read_csv("../data/brent_oil_prices.csv")
events = pd.read_csv("../data/events.csv")


@app.get("/")
def home():
    return {"message": "Brent Oil API"}


@app.get("/prices")
def get_prices():
    return jsonify(prices.to_dict(orient="records"))


@app.get("/events")
def get_events():
    return jsonify(events.to_dict(orient="records"))


@app.get("/changepoints")
def get_change_points():
    return jsonify({
        "status": "placeholder",
        "message": "Bayesian change point results"
    })


if __name__ == "__main__":
    app.run(debug=True)