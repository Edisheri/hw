import pytest
import requests
from hw4.tests.models import DogRandomImage, DogBreedList, DogErrorResponse, DogSubBreedList

BASE_URL = "https://dog.ceo/api"

@pytest.mark.parametrize("breed", ["hound", "terrier", "bulldog"])
def test_random_image_by_breed(breed):
    response = requests.get(f"{BASE_URL}/breed/{breed}/images/random")
    assert response.status_code == 200
    DogRandomImage.model_validate(response.json())

def test_all_breeds_list():
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    assert response.status_code == 200
    DogBreedList.model_validate(response.json())

@pytest.mark.parametrize("breed, subbreeds", [
    ("hound", ["afghan", "basset", "blood"]),
    ("terrier", ["american", "bedlington", "border"])
])
def test_subbreeds_list(breed, subbreeds):
    response = requests.get(f"{BASE_URL}/breed/{breed}/list")
    assert response.status_code == 200
    data = DogSubBreedList.model_validate(response.json())
    assert set(subbreeds).issubset(data.message)

def test_invalid_breed():
    response = requests.get(f"{BASE_URL}/breed/invalid_breed/images")
    assert response.status_code == 404
    DogErrorResponse.model_validate(response.json())

@pytest.mark.parametrize("number", [1, 3, 5])
def test_multiple_random_images(number):
    response = requests.get(f"{BASE_URL}/breeds/image/random/{number}")
    assert response.status_code == 200
    data = response.json()
    assert len(data["message"]) == number