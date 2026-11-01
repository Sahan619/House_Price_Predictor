from flask import Flask, render_template, request
import joblib
import pandas as pd
import math

app = Flask(__name__)

# Load the trained model
model = joblib.load("models/house_price_model.pkl")


# Feature order must match the order used during training
FEATURES = [
    "Avg. Area Income",
    "Avg. Area House Age",
    "Avg. Area Number of Rooms",
    "Avg. Area Number of Bedrooms",
    "Area Population"
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get values from the HTML form
        income = float(request.form["income"])
        house_age = float(request.form["house_age"])
        rooms = float(request.form["rooms"])
        bedrooms = float(request.form["bedrooms"])
        population = float(request.form["population"])

        # Check for invalid numbers
        values = [income, house_age, rooms, bedrooms, population]

        if not all(math.isfinite(value) for value in values):
            raise ValueError

        # Basic validation
        if income <= 0:
            return render_template(
                "index.html",
                error="Income must be greater than 0."
            )

        if house_age <= 0:
            return render_template(
                "index.html",
                error="House age must be greater than 0."
            )

        if rooms <= 0:
            return render_template(
                "index.html",
                error="Number of rooms must be greater than 0."
            )

        if bedrooms <= 0:
            return render_template(
                "index.html",
                error="Number of bedrooms must be greater than 0."
            )

        if population <= 0:
            return render_template(
                "index.html",
                error="Population must be greater than 0."
            )

        # Create DataFrame with the same feature names
        features = pd.DataFrame(
            [[income, house_age, rooms, bedrooms, population]],
            columns=FEATURES
        )

        # Make prediction
        prediction = model.predict(features)[0]

        return render_template(
            "index.html",
            prediction=f"${prediction:,.2f}"
        )

    except (ValueError, TypeError, KeyError):
        return render_template(
            "index.html",
            error="Please enter valid numerical values."
        )


if __name__ == "__main__":
    app.run(debug=True)