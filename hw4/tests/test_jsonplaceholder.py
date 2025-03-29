import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 100

@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_post_by_id(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id

def test_create_post():
    new_post = {"title": "Test", "body": "Test body", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 101
    assert data["title"] == "Test"

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.json() == {}

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_comments_by_post_id(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}/comments")
    assert response.status_code == 200
    data = response.json()
    assert all(comment["postId"] == post_id for comment in data)