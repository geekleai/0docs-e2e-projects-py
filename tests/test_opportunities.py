from fastapi.testclient import TestClient
from app.main import app
from app.schemas.opportunity import Opportunity

client = TestClient(app)

def test_create_opportunity():
    response = client.post("/opportunities/", json={"title": "New Opportunity", "description": "Opportunity description", "value": 10000})
    assert response.status_code == 201
    assert response.json()["title"] == "New Opportunity"

def test_get_opportunity():
    response = client.get("/opportunities/1")
    assert response.status_code == 200
    assert "title" in response.json()

def test_update_opportunity():
    response = client.put("/opportunities/1", json={"title": "Updated Opportunity", "description": "Updated description", "value": 15000})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Opportunity"

def test_delete_opportunity():
    response = client.delete("/opportunities/1")
    assert response.status_code == 204

def test_get_all_opportunities():
    response = client.get("/opportunities/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)