from flask import request, jsonify, Blueprint
from app.models.admins import AdminUser

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admins", methods=["GET"])
def get_all_admins():
    admins = AdminUser.query.all()
    admin_list = [
        {"id": admin.id, "username": admin.username, "email": admin.email}
        for admin in admins
    ]
    return jsonify(admin_list)


@admin_bp.route("/admins/create", methods=["POST"])
def create_admin_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400
    
    # Create a new admin user using the create method of AdminUser model
    new_admin_user = AdminUser.create(username=username, email=email, password=password)
    
    if new_admin_user:
        return jsonify(
            {
                "message": "Admin user created successfully",
                "admin_user": {
                    "id": new_admin_user.id,
                    "username": new_admin_user.username,
                    "email": new_admin_user.email
                }
            }
        ), 201
    else:
        return jsonify({"error": "Failed to create admin user"}), 500
