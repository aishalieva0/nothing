from flask import request, jsonify, Blueprint
from app import app
from app.models.companies import Company

company_bp = Blueprint("company", __name__)


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
