
from unittest.mock import patch

from fastapi.testclient import TestClient
from sqlalchemy import text

from database import engine
from main import app


client = TestClient(app)


def test_health():
    with patch("main.redis_client.ping", return_value=True):
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["redis"] == "healthy"


def test_postgres_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1")).scalar()

    assert result == 1
