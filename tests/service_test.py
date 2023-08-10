import pytest
from recruitment.service import app


@pytest.fixture()
def client():
    return app.test_client()


def test_feedback_endpoint_returns_200(client):
    response = client.post("/feedback", json={"feedback": "The employee did well"})
    assert response.status_code == 200


def test_feedback_endpoint_returns_400_given_no_feedback(client):
    response = client.post("/feedback", json={})
    assert response.status_code == 400


def test_feedback_endpoint_returns_400_given_invalid_feedback(client):
    response = client.post("/feedback", json={"feedback": ""})
    assert response.status_code == 400
