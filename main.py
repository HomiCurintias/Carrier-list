from flask import Flask, render_template, request, jsonify, session
from pymongo import MongoClient
from argon2 import PasswordHasher
import os

MONGO_URI = os.getenv("mongo_url")
client = MongoClient(MONGO_URI)
db = client["data-base"]
users = db["users"]

ph = PasswordHasher()

app = Flask(__name__)
app.secret_key = os.getenv("secret") or "uma_chave_secreta_aqui"

def get_users_doc():
    doc = users.find_one({"_id": "users_data"})
    if not doc:
        users.insert_one({"_id": "users_data"})
        doc = {"_id": "users_data"}
    return doc

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("user")
    password = data.get("pass")

    if not username or not password:
        return jsonify({"error": "missing fields"}), 400

    doc = get_users_doc()

    if username in doc:
        return jsonify({"error": "user already exists"}), 400

    hashed = ph.hash(password)
    users.update_one(
        {"_id": "users_data"},
        {"$set": {username: hashed}}
    )

    session["user"] = username

    return jsonify({"status": "created"}), 201

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()

    user = data.get("user")
    password = data.get("pass")

    if not user or not password:
        return jsonify({"error": "missing fields"}), 400

    doc = get_users_doc()

    if user not in doc:
        return jsonify({"status": "user_not_found"}), 404

    try:
        ph.verify(doc[user], password)
        session["user"] = user
        return jsonify({"status": "logged"}), 200
    except:
        return jsonify({"status": "wrong_password"}), 403

@app.route("/api/me", methods=["GET"])
def me():
    if "user" in session:
        return jsonify({"logged_in_as": session["user"]})
    return jsonify({"logged_in_as": None})

# Logout
@app.route("/api/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return jsonify({"status": "logged_out"}), 200

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

@app.route("/login")
def loginFront():
    return render_template("login.html")

@app.route("/register")
def registerFront():
    return render_template("register.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
