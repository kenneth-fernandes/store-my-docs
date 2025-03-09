import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "port": os.getenv("DB_PORT"),
}

JWT_CONFIG = {
    "secret": os.getenv("JWT_SECRET")
}

SWAGGER_API_CONFIG = {
    "app": {
        "swagger_json": {
            "info": {
                "title": "Store My Docs API",
                "version": "1.0",
                "description": "API Documentation for Store My Docs",
            },
            "basePath": "/api",
            "schemes": ["http"],
            "openapi": "3.0.2"
        }
    },
    "auth": {
        "register": {
            "tags": ["Authentication"],
            "summary": "Register a new user",
            "parameters": [
                {
                    "name": "body",
                    "in": "body",
                    "required": True,
                    "schema": {
                        "example": {
                            "username": "testuser",
                            "email": "test@example.com",
                            "password": "securepassword"
                        }
                    }
                }
            ],
            "responses": {
                "201": {"description": "User registered"},
                "400": {"description": "Missing fields"},
                "500": {"description": "User registration failed"}
            }
        },
        "login": {
            "tags": ["Authentication"],
            "summary": "User Login",
            "parameters": [
                {
                    "name": "body",
                    "in": "body",
                    "required": True,
                    "schema": {
                        "example": {
                            "identifier": "testuser or test@example.com",
                            "password": "securepassword"
                        }
                    }
                }
            ],
            "responses": {
                "200": {"description": "Login successful"},
                "400": {"description": "Missing fields"},
                "401": {"description": "Authentication failed"},
                "404": {"description": "User not found"}
            }
        }
    },
    "documents": {
        "get_user_documents": {
            "tags": ["Documents"],
            "summary": "Get all documents for logged-in user",
            "responses": {
                "200": {"description": "Returns a list of documents"},
                "401": {"description": "Unauthorized"},
                "404": {"description": "Documents not found"}
            }
        },
        "get_document_by_id": {
            "tags": ["Documents"],
            "summary": "Get a specific document by ID",
            "parameters": [
                {
                    "name": "doc_id",
                    "in": "path",
                    "required": True,
                    "type": "integer"
                }
            ],
            "responses": {
                "200": {"description": "Returns the document details"},
                "401": {"description": "Unauthorized"},
                "404": {"description": "Document not found"}
            }
        },
        "upload_document": {
            "tags": ["Documents"],
            "summary": "Upload a document",
            "parameters": [
                {
                    "name": "body",
                    "in": "body",
                    "required": True,
                    "schema": {
                        "example": {
                            "filename": "document.pdf",
                            "file_url": "https://s3.amazonaws.com/bucket/document.pdf"
                        }
                    }
                }
            ],
            "responses": {
                "201": {"description": "Document uploaded successfully"},
                "400": {"description": "Missing fields"},
                "401": {"description": "Unauthorized"},
                "500": {"description": "Upload failed"}
            }
        },
        "delete_document": {
            "tags": ["Documents"],
            "summary": "Delete a document",
            "parameters": [
                {
                    "name": "doc_id",
                    "in": "path",
                    "required": True,
                    "type": "integer"
                }
            ],
            "responses": {
                "200": {"description": "Document deleted"},
                "400": {"description": "Missing doc_id"},
                "401": {"description": "Unauthorized"},
                "404": {"description": "Document not found"}
            }
        }
    }
}

SWAGGER = {
    "title": "Store My Docs API",
    "uiversion": 3,
    "version": "1.0",
    "description": "API Documentation for Store My Docs",
    "termsOfService": "",
    "specs_route": "/apidocs/",
    "openapi": "3.0.2",
}

CONTENT_SECURITY_POLICY = {
    'default-src': [
        "'self'",
        "https://fonts.googleapis.com",
        "https://cdnjs.cloudflare.com",
        "https://unpkg.com",
        "https://cdn.jsdelivr.net",
    ],
    'style-src': [
        "'self'",
        "'unsafe-inline'",
        "https://fonts.googleapis.com",
        "https://cdnjs.cloudflare.com",
        "https://unpkg.com",
        "https://cdn.jsdelivr.net",
    ],
    'script-src': [
        "'self'",
        "'unsafe-inline'",
        "'unsafe-eval'",
        "https://cdnjs.cloudflare.com",
        "https://unpkg.com",
        "https://cdn.jsdelivr.net",
    ]
}