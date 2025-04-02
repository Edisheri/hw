import pytest
import requests
from hw4.tests.models import Post, Posts, Comments

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    Posts.model_validate(response.json())

@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_post_by_id(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    Post.model_validate(response.json())

def test_create_post():
    new_post = {"title": "Test", "body": "Test body", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    Post.model_validate(response.json())

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_comments_by_post_id(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}/comments")
    assert response.status_code == 200
    Comments.model_validate(response.json())

@pytest.mark.parametrize("post_id", [1])
def test_update_post(post_id):
    updated_data = {"title": "Updated Title"}
    response = requests.patch(f"{BASE_URL}/posts/{post_id}", json=updated_data)
    assert response.status_code == 200
    Post.model_validate(response.json())