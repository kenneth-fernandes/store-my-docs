from flask import Blueprint, request, jsonify
from models.document import Document

document_bp = Blueprint("documents", __name__)

# Get all documents
@document_bp.route("/documents", methods=["GET"])
def get_all_documents():
    docs = Document.get_all_documents()
    return jsonify(docs), 200

# Get a specific document
@document_bp.route("/documents/<int:doc_id>", methods=["GET"])
def get_document_by_id(doc_id):
    doc = Document.get_document_by_id(doc_id)
    if doc:
        return jsonify(doc), 200
    return jsonify({"error": f"Document with 'doc_id = {doc_id}' not found"}), 404

# Upload a document
@document_bp.route("/documents", methods=["POST"])
def upload_document():
    data = request.get_json()
    filename =  data["filename"]
    file_url = data["file_url"]

    if not filename or not file_url:
        jsonify({"error": "Missing filename or file_url"}), 400

    doc_id = Document.insert_document(filename, file_url)
    return jsonify({"message": "Document uploaded!", "doc_id": doc_id}), 201

# Delete a document
@document_bp.route("/documents/<int:doc_id>", methods=["DELETE"])
def delete_document(doc_id):
    success = Document.delete_document(doc_id)
    if success:
        return jsonify({"message": "Document deleted!"}), 200
    return jsonify({"error": "Document not found"}), 404