from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app
from app.schemas.customer import Customer

client = TestClient(app)

def test_create_customer():
    response = client.post("/customers/", json={"id": 1, "name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john@example.com"}

def test_get_customer():
    response = client.get("/customers/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john@example.com"}

def test_update_customer():
    response = client.put("/customers/1", json={"name": "John Smith", "email": "johnsmith@example.com"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Smith", "email": "johnsmith@example.com"}

def test_delete_customer():
    response = client.delete("/customers/1")
    assert response.status_code == 204

def test_get_nonexistent_customer():
    response = client.get("/customers/999")
    assert response.status_code == 404