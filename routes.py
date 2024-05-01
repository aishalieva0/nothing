from flask import request, jsonify
from app import app
from models.users import User
from models.admins import AdminUser
from models.problems import Problem
from models.companies import Company


@app.route("/admin/users", methods=["POST"])
def create_admin_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400
    new_admin_user = AdminUser.create(username, email)
    return jsonify(
        {
            "message": "Admin user created successfully",
            "admin_user": new_admin_user.__dict__,
        }
    )


@app.route("/admin/users", methods=["GET"])
def get_admin_users():
    admin_users = AdminUser.get_all()
    return jsonify([admin_user.__dict__ for admin_user in admin_users])


@app.route("/companies", methods=["POST"])
def create_company():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400
    new_company = Company.create(name, email)
    return jsonify(
        {"message": "Company created successfully", "company": new_company.__dict__}
    )


@app.route("/companies", methods=["GET"])
def get_companies():
    companies = Company.get_all()
    return jsonify([company.__dict__ for company in companies])


@app.route("/problems", methods=["POST"])
def create_problem():
    data = request.get_json()
    user_id = data.get("user_id")
    company_id = data.get("company_id")
    description = data.get("description")
    if not user_id or not company_id or not description:
        return (
            jsonify({"error": "User ID, Company ID, and Description are required"}),
            400,
        )
    new_problem = Problem.create(user_id, company_id, description)
    return jsonify(
        {"message": "Problem created successfully", "problem": new_problem.__dict__}
    )


@app.route("/problems", methods=["GET"])
def get_problems():
    problems = Problem.get_all()
    return jsonify([problem.__dict__ for problem in problems])


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
