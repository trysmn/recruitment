import pytest
from recruitment.service import app


@pytest.fixture()
def client():
    return app.test_client()


def test_feedback_endpoint_returns_200(client):
    response = client.post("/feedback", json={"feedback": "The employee did well"})
    assert response.status_code == 200
