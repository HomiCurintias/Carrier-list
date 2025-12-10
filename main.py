from flask import Flask, render_template

import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/legacy")
def legacy():
    return render_template("legacy.html")

@app.route("/players")
def players():
    return render_template("players.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
