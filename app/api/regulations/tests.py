from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

valid_token = "valid_token_here"


def test_create_regulation():
    regulation_data = {
        "article_id": 1,
        "title": "Regulation 1",
        "content": "Content of Regulation 1"
    }
    response = client.post("/regulations", json=regulation_data, headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["article_id"] == 1
    assert data["title"] == "Regulation 1"


def test_read_all_regulations():
    response = client.get("/regulations", headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    data = response.json()


def test_read_regulations_by_article_id():
    response = client.get("/regulations/1", headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    data = response.json()


def test_update_regulation():
    regulation_data = {
        "article_id": 1,
        "title": "Updated Regulation 1",
        "content": "Updated Content of Regulation 1"
    }
    response = client.put("/regulations/1", json=regulation_data, headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Regulation 1"


def test_delete_regulation():
    response = client.delete("/regulations/1", headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    data = response.text
    assert data == "Regulation 1 successfully deleted"


