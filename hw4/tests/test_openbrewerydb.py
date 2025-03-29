import pytest
import requests

BASE_URL = "https://api.openbrewerydb.org/v1/breweries"


@pytest.mark.parametrize("state", ["new_york", "california", "texas"])
def test_breweries_by_state(state):
    response = requests.get(f"{BASE_URL}?by_state={state}")
    assert response.status_code == 200
    data = response.json()
    assert all(brewery["state"].lower() == state.replace("_", " ") for brewery in data)


def test_get_brewery_by_id():
    # Динамический поиск актуального ID
    search_response = requests.get(f"{BASE_URL}?by_name=madtree")
    assert search_response.status_code == 200
    breweries = search_response.json()

    assert len(breweries) > 0, "Пивоварня MadTree не найдена"
    valid_id = breweries[0]["id"]

    response = requests.get(f"{BASE_URL}/{valid_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == valid_id
    assert "MadTree" in data["name"]


@pytest.mark.parametrize("city, state", [
    ("san_diego", "california"),
    ("austin", "texas")
])
def test_breweries_by_city(city, state):
    response = requests.get(f"{BASE_URL}?by_city={city}&by_state={state}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert all(brewery["city"].lower() == city.replace("_", " ") for brewery in data)


def test_invalid_brewery_id():
    response = requests.get(f"{BASE_URL}/invalid_id_123")
    assert response.status_code == 404


@pytest.mark.parametrize("brewery_type", ["micro", "regional", "brewpub"])
def test_breweries_by_type(brewery_type):
    response = requests.get(f"{BASE_URL}?by_type={brewery_type}")
    assert response.status_code == 200
    data = response.json()
    assert all(brewery["brewery_type"] == brewery_type for brewery in data)