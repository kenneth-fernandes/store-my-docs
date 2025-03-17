import pytest
from models.user import User
from models.document import Document

def test_create_user():
    user_id = User.create_user("testuser_model", "testuser@example.com", "securepassword@123")
    assert user_id is not None

def test_find_user():
    user = User.find_user_by_username_or_email("testuser@example.com")
    assert user is not None

def test_insert_document():
    doc_id = Document.insert_document("test_doc.pdf", "https://example.com/doc.pdf", 1)
    assert doc_id is not None

def test_get_documents_by_user():
    docs = Document.get_documents_by_user(1)
    assert isinstance(docs, list)
