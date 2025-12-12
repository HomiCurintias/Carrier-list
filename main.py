from flask import Flask, render_template, request, jsonify, session
from pymongo import MongoClient
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import os

MONGO_URI = os.getenv("mongo_url")

client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000,
    tlsAllowInvalidCertificates=True
)

db = client["data-base"]
users = db["users"]

ph = PasswordHasher()

app = Flask(__name__)
app.secret_key = os.getenv("secret")

if os.getenv("ENVIRONMENT") == "production":
    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax'
    )

def get_users_doc():
    try:
        doc = users.find_one({"_id": "users_data"})
        if not doc:
            users.insert_one({"_id": "users_data"})
            doc = {"_id": "users_data"}
        return doc
    except Exception as e:
        print(f"Database error: {e}")
        return None

@app.route("/api/register", methods=["POST"])
def register():
    try:
        data = request.get_json()
        username = data.get("user")
        password = data.get("pass")
        
        if not username or not password:
            return jsonify({"error": "missing fields"}), 400
        
        if len(username) < 3 or len(username) > 30:
            return jsonify({"error": "username must be 3-30 characters"}), 400
        
        if len(password) < 6:
            return jsonify({"error": "password must be at least 6 characters"}), 400
        
        doc = get_users_doc()
        if not doc:
            return jsonify({"error": "database error"}), 500
        
        if username in doc:
            return jsonify({"error": "user already exists"}), 400
        
        hashed = ph.hash(password)
        users.update_one(
            {"_id": "users_data"},
            {"$set": {username: hashed}}
        )
        
        session["user"] = username
        return jsonify({"status": "created"}), 201
        
    except Exception as e:
        print(f"Registration error: {e}")
        return jsonify({"error": "registration failed"}), 500

@app.route("/api/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        user = data.get("user")
        password = data.get("pass")
        
        if not user or not password:
            return jsonify({"error": "missing fields"}), 400
        
        doc = get_users_doc()
        if not doc:
            return jsonify({"error": "database error"}), 500
        
        if user not in doc:
            return jsonify({"status": "user_not_found"}), 404
        
        try:
            ph.verify(doc[user], password)
            session["user"] = user
            return jsonify({"status": "logged"}), 200
        except VerifyMismatchError:
            return jsonify({"status": "wrong_password"}), 403
            
    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({"error": "login failed"}), 500

@app.route("/me", methods=["GET"])
def me():
    if "user" in session:
        return f"""hi, {session["user"]} <br><a href="/logout">Logout</a>"""
    
    return redirect("/login")

@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user", None)
    
    return redirect("/")

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
    app.run(host="0.0.0.0", port=port, debug=True)
