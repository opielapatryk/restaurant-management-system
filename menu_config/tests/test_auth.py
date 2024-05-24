# Third party modules
from fastapi.testclient import TestClient

# Local modules
from main import app

client = TestClient(app)

def test_login():
    response = client.post("/login", json={"email": "email", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()

def test_refresh_token():
    login_response = client.post("/login", json={"email": "email", "password": "password"})
    refresh_token = login_response.json()["refresh_token"]
    response = client.post("/refresh-token", json={"token": refresh_token})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()

def test_verify_token():
    login_response = client.post("/login", json={"email": "email", "password": "password"})
    access_token = login_response.json()["access_token"]
    response = client.post("/verify-token", json={"token": access_token})
    assert response.status_code == 200
    assert response.json()["message"] == "Token is valid"
