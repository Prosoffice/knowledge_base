from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


valid_token = "valid_token_here"


def test_create_gdpr_article():
    article_data = {
        "article_number": "GDPR-001",
        "title": "Article 1"
    }
    response = client.post("/gdpr_articles", json=article_data, headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["article_number"] == "GDPR-001"
    assert data["title"] == "Article 1"


def test_read_all_gdpr_articles():
    response = client.get("/gdpr_articles", headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200


def test_read_gdpr_article_by_id():
    response = client.get("/gdpr_articles/1", headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


def test_update_gdpr_article():
    article_data = {
        "article_number": "GDPR-001",
        "title": "Updated Article 1"
    }
    response = client.put("/gdpr_articles/1", json=article_data, headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Article 1"


def test_delete_gdpr_article():
    response = client.delete("/gdpr_articles/1", headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    data = response.text
    assert data == "Article 1 successfully deleted"
