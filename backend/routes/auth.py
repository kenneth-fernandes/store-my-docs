import logging

from flasgger import swag_from
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from extensions import limiter
from models.user import User
from flask import Blueprint, jsonify, request
import datetime
import json
from config import SWAGGER_API_CONFIG

auth_bp = Blueprint("auth", __name__)
bcrypt = Bcrypt()

# Register user
@auth_bp.route("/register", methods=["POST"])
@limiter.limit("5 per hour")
@swag_from(SWAGGER_API_CONFIG["auth"]["register"])
def register():
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]

    if not username or not email or not password:
        logging.warning("User registration failed: Missing required fields.")
        return jsonify({"error": "Fields are missing!"}), 400

    user_id = User.create_user(username, email, password)
    if not user_id:
        logging.error(f"User registration failed for {email}.")
        return jsonify({"error": "User registration failed!"}), 500

    logging.info(f"User registered successfully: {username} ({email}) - User ID: {user_id}")
    return jsonify({"message": "User registered!", "user_id": user_id}), 201

# User login
@auth_bp.route("/login", methods=["POST"])
@limiter.limit("10 per hour")
@swag_from(SWAGGER_API_CONFIG["auth"]["login"])
def login():
    data = request.get_json()
    identifier = data["identifier"]
    password = data["password"]

    if not identifier or not password:
        logging.warning("Login attempt failed: Missing credentials.")
        return jsonify({"error": "Fields are missing!"}), 400

    user = User.find_user_by_username_or_email(identifier)
    if not user:
        logging.warning(f"Login attempt failed: User '{identifier}' not found.")
        return jsonify({"error": "User could not be found!"}), 404

    if not bcrypt.check_password_hash(user.password_hash, password):
        logging.warning(f"Login failed: Incorrect password for user '{identifier}'.")
        return jsonify({"error": "User authentication failed!"}), 401

    user_data = json.dumps({"user_id": user.id, "user_role" : user.role})

    access_token = create_access_token(identity=user_data, expires_delta=datetime.timedelta(days=1))

    logging.info(f"User login successful: {identifier} (Role: {user.role})")
    return jsonify({"message" : "Login successful!", "role": user.role, "access_token" : access_token}), 200
