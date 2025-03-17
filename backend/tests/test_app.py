import requests

BASE_URL = "http://127.0.0.1:5001"

def test_api_status():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "API is running!" in response.text

def test_swagger_json():
    response = requests.get(f"{BASE_URL}/apidocs/swagger.json")
    assert response.status_code == 200
