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

@auth_bp.route("/users", methods=["GET"])
def get_users():
    users = AuthController.get_users()
    return jsonify({"message": "Successfully retrieved users", "users": users}), 200
