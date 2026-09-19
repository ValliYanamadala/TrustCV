from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_health_root():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "TrustCV"
    assert data["version"] == "0.1.0"
    assert "operational" in data["message"].lower()


def test_health_api_v1():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "TrustCV"
    assert data["version"] == "0.1.0"
