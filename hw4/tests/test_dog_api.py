import pytest
import requests

BASE_URL = "https://dog.ceo/api"

@pytest.mark.parametrize("breed", ["hound", "terrier", "bulldog"])
def test_random_image_by_breed(breed):
    response = requests.get(f"{BASE_URL}/breed/{breed}/images/random")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data and "status" in data
    assert data["status"] == "success"

def test_all_breeds_list():
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["message"], dict)
    assert len(data["message"]) > 0

@pytest.mark.parametrize("breed, subbreeds", [
    ("hound", ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"]),
    ("terrier", ["american", "bedlington", "border", "cairn", "dandie", "fox",
                "irish", "kerryblue", "lakeland", "norfolk", "norwich",
                "patterdale", "russell", "scottish", "sealyham", "silky",
                "tibetan", "toy", "welsh", "westhighland", "wheaten", "yorkshire"])
])
def test_subbreeds_list(breed, subbreeds):
    response = requests.get(f"{BASE_URL}/breed/{breed}/list")
    assert response.status_code == 200
    data = response.json()
    assert set(subbreeds).issubset(set(data["message"])), f"Missing subbreeds for {breed}"

def test_invalid_breed():
    response = requests.get(f"{BASE_URL}/breed/invalid_breed/images")
    assert response.status_code == 404
    assert response.json()["status"] == "error"

@pytest.mark.parametrize("number", [1, 3, 5])
def test_multiple_random_images(number):
    response = requests.get(f"{BASE_URL}/breeds/image/random/{number}")
    assert response.status_code == 200
    data = response.json()
    assert len(data["message"]) == number