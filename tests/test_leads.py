from fastapi.testclient import TestClient
from app.main import app
from app.schemas.lead import Lead

client = TestClient(app)

def test_create_lead():
    response = client.post("/leads/", json={"id": 1, "name": "Lead 1", "email": "lead1@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Lead 1", "email": "lead1@example.com"}

def test_get_lead():
    response = client.get("/leads/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Lead 1", "email": "lead1@example.com"}

def test_update_lead():
    response = client.put("/leads/1", json={"name": "Updated Lead 1", "email": "updated_lead1@example.com"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Updated Lead 1", "email": "updated_lead1@example.com"}

def test_delete_lead():
    response = client.delete("/leads/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Lead deleted successfully"}

def test_get_nonexistent_lead():
    response = client.get("/leads/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Lead not found"}