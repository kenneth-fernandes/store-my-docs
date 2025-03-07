from flask import Blueprint, request, jsonify
from models.document import Document
from flask_jwt_extended import jwt_required, get_jwt

document_bp = Blueprint("documents", __name__)

def is_admin(user):
    return user["role"].lower() == "admin"


# Get all documents
@document_bp.route("/documents", methods=["GET"])
@jwt_required()
def get_user_documents():
    data = get_jwt()
    user_id = data.get("sub")

    docs = Document.get_documents_by_user(user_id)
    if len(docs) == 0:
        return jsonify({"error": "Documents not found or unauthorized"}), 404

    return jsonify(docs), 200


# Get a specific document
@document_bp.route("/documents/<int:doc_id>", methods=["GET"])
@jwt_required()
def get_document_by_id(doc_id):
    data = get_jwt()
    user_id = data.get("sub")

    doc = Document.get_document_by_id(doc_id, user_id)
    if doc:
        return jsonify(doc), 200
    return jsonify({"error": "Document not found or unauthorized"}), 404


# Upload a document
@document_bp.route("/documents", methods=["POST"])
@jwt_required()
def upload_document():
    data = get_jwt()
    user_id = data.get("sub")

    data = request.get_json()
    filename =  data["filename"]
    file_url = data["file_url"]

    if not filename or not file_url:
        return jsonify({"error": "Missing filename or file_url"}), 400

    doc_id = Document.insert_document(filename, file_url, user_id)
    if doc_id is None:
        return jsonify({"error": "Failed to upload document"}), 500
    return jsonify({"message": "Document uploaded!", "doc_id": doc_id}), 201


# Delete a document
@document_bp.route("/documents/<int:doc_id>", methods=["DELETE"])
@jwt_required()
def delete_document(doc_id):
    data = get_jwt()
    user_id = data.get("sub")

    success = Document.delete_document(doc_id, user_id)
    if success:
        return jsonify({"message": "Document deleted!"}), 200
    return jsonify({"error": "Document not found or unauthorized"}), 404