from flask import Flask, request, render_template
import numpy as np
import pandas as pd


application = Flask(__name__)

app = application

## Route for a home page


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")


if __name__ == "__main__":
    # app.run(host="0.0.0.0",port=8080)
    app.run(host="0.0.0.0", port=8000)
