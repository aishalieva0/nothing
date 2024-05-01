from flask import request, jsonify, Blueprint
from app import app
from app.models.users import User

user_bp = Blueprint("user", __name__)


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400
    new_user = User.create(username, email)
    return jsonify({"message": "User created successfully", "user": new_user.__dict__})


@app.route("/users", methods=["GET"])
def get_users():
    users = User.get_all()
    return jsonify([user.__dict__ for user in users])
