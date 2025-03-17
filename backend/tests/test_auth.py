import requests

BASE_URL = "http://127.0.0.1:5001/api"

def test_register_user():
    payload = {"username": "test_user", "email": "test@example.com", "password": "securepassword@123"}
    response = requests.post(f"{BASE_URL}/register", json=payload)
    assert response.status_code in [201, 400]  # 400 if user already exists

def test_login_user():
    payload = {"identifier": "test_user", "password": "securepassword@123"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()
