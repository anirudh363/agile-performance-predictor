from flask import Blueprint, request, jsonify
from controllers.auth_controller import AuthController

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    result = AuthController.signup(data["name"], data["email"], data["password"])
    
    if "error" in result:
        return jsonify({"message": result["error"]}), 409  # Conflict
    return jsonify({"message": "User registered and logged in successfully", "data": result}), 201  # Created

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    result = AuthController.login(data["email"], data["password"])
    
    if "error" in result:
        return jsonify({"message": result["error"]}), 401  # Unauthorized
    return jsonify({"message": "Login successful", "data": result}), 200  # OK

@auth_bp.route("/change-password", methods=["POST"])
def change_password():
    data = request.get_json()
    result = AuthController.change_password(data["email"], data["old_password"], data["new_password"])
    
    if "error" in result:
        return jsonify({"message": result["error"]}), 404
    return jsonify({"message": "Password changed successfully", "data": result}), 200


@auth_bp.route("/users", methods=["GET"])
def get_users():
    users = AuthController.get_users()
    return jsonify({"message": "Successfully retrieved users", "users": users}), 200

@auth_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = AuthController.get_user_by_id(user_id)
    if user:
        return jsonify({"message": "Successfully retrieved user", "user": user}), 200
    return jsonify({"message": "User not found"}), 404

@auth_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = AuthController.update_user(user_id, data)
    if user:
        return jsonify({"message": "User updated successfully", "user": user}), 200
    return jsonify({"message": "User not found"}), 404

@auth_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = AuthController.get_user_by_id(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    status = AuthController.delete_user(user_id)
    if status:
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "User not found"}), 404
