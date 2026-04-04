from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_status_returns_200():
    response = client.get("/status")
    assert response.status_code == 200


def test_status_response_fields():
    response = client.get("/status")
    data = response.json()
    assert "app_name" in data
    assert "version" in data
    assert "environment" in data
    assert "status" in data
    assert "timestamp" in data


def test_status_values():
    response = client.get("/status")
    data = response.json()
    assert data["app_name"] == "OrgWide Session Demo"
    assert data["version"] == "v1"
    assert data["status"] == "All systems operational"


def test_status_timestamp_is_iso():
    from datetime import datetime
    response = client.get("/status")
    data = response.json()
    datetime.fromisoformat(data["timestamp"])
