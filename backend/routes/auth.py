from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from models.user import User
from flask import Blueprint, jsonify, request
import datetime

auth_bp = Blueprint("auth", __name__)
bcrypt = Bcrypt()

# Register user
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]

    if not username or not email or not password:
        return jsonify({"error": "Fields are missing!"}), 400

    user_id = User.create_user(username, email, password)
    if not user_id:
        return jsonify({"error": "User registration failed!"}), 500

    return jsonify({"message": "User registered!", "user_id": user_id}), 201

# User login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    identifier = data["identifier"]
    password = data["password"]

    if not identifier or not password:
        return jsonify({"error": "Fields are missing!"}), 400

    user = User.find_user_by_username_or_email(identifier)
    if not user:
        return jsonify({"error": "User could not be found!"}), 404

    if not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({"error": "User authentication failed!"}), 401

    access_token = create_access_token(identity=str(user.id),
                                   additional_claims={"role": user.role},
                                   expires_delta=datetime.timedelta(days=1))
    return jsonify({"message" : "Login successful!", "role": user.role, "access_token" : access_token}), 200
