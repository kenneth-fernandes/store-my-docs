import json
from flasgger import swag_from
from flask import Blueprint, request, jsonify
from models.document import Document
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import limiter
from config import SWAGGER_API_CONFIG

document_bp = Blueprint("documents", __name__)

def is_admin(user):
    return user["role"].lower() == "admin"


# Get all documents
@document_bp.route("/documents", methods=["GET"])
@jwt_required()
@limiter.limit("30 per minute")
@swag_from(SWAGGER_API_CONFIG["documents"]["get_user_documents"])
def get_user_documents():
    identity_str = get_jwt_identity()
    user = json.loads(identity_str)
    user_id = user["user_id"]

    docs = Document.get_documents_by_user(user_id)
    if len(docs) == 0:
        return jsonify({"error": "Documents not found or unauthorized"}), 404

    return jsonify(docs), 200


# Get a specific document
@document_bp.route("/documents/<int:doc_id>", methods=["GET"])
@jwt_required()
@limiter.limit("30 per minute")
@swag_from(SWAGGER_API_CONFIG["documents"]["get_document_by_id"])
def get_document_by_id(doc_id):
    identity_str = get_jwt_identity()
    user = json.loads(identity_str)
    user_id = user["user_id"]

    doc = Document.get_document_by_id(doc_id, user_id)
    if doc:
        return jsonify(doc), 200
    return jsonify({"error": "Document not found or unauthorized"}), 404


# Upload a document
@document_bp.route("/documents", methods=["POST"])
@jwt_required()
@limiter.limit("10 per day")
@swag_from(SWAGGER_API_CONFIG["documents"]["upload_document"])
def upload_document():
    identity_str = get_jwt_identity()
    user = json.loads(identity_str)
    user_id = user["user_id"]

    data = request.get_json()
    filename =  data["filename"]
    file_url = data["file_url"]

    if not filename or not file_url or not user_id:
        return jsonify({"error": "Missing filename or file_url or user_id"}), 400

    doc_id = Document.insert_document(filename, file_url, user_id)
    if doc_id is None:
        return jsonify({"error": "Failed to upload document"}), 500
    return jsonify({"message": "Document uploaded!", "doc_id": doc_id}), 201


# Delete a document
@document_bp.route("/documents/<int:doc_id>", methods=["DELETE"])
@jwt_required()
@limiter.limit("5 per hour")
@swag_from(SWAGGER_API_CONFIG["documents"]["delete_document"])
def delete_document(doc_id):
    identity_str = get_jwt_identity()
    user = json.loads(identity_str)
    user_id = user["user_id"]

    if not doc_id or not user_id:
        return jsonify({"error": "Missing doc_id or user_id"}), 400

    success = Document.delete_document(doc_id, user_id)
    if success:
        return jsonify({"message": "Document deleted!"}), 200
    return jsonify({"error": "Document not found or unauthorized"}), 404