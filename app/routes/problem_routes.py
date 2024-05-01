from flask import request, jsonify, Blueprint
from app import app
from app.models.problems import Problem

problem_bp = Blueprint("problem", __name__)


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
