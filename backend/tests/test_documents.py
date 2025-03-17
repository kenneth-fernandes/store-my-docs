import requests

BASE_URL = "http://127.0.0.1:5001/api"


def get_auth_token():
    response = requests.post(f"{BASE_URL}/login", json={"identifier": "test_user", "password": "securepassword@123"})
    return response.json().get("access_token")


def test_upload_document():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"filename": "test.pdf", "file_url": "https://example.com/test.pdf"}

    response = requests.post(f"{BASE_URL}/documents", json=payload, headers=headers)
    assert response.status_code == 201
    assert "doc_id" in response.json()


def test_get_documents():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(f"{BASE_URL}/documents", headers=headers)
    assert response.status_code == 200


def test_delete_document():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    # Assuming we delete the first document
    response = requests.delete(f"{BASE_URL}/documents/1", headers=headers)
    assert response.status_code in [200, 404]  # 200 if found, 404 if already deleted
