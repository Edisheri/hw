import pytest
import requests
from hw4.tests.models import Brewery, Breweries

BASE_URL = "https://api.openbrewerydb.org/v1/breweries"

@pytest.mark.parametrize("state", ["new_york", "california", "texas"])
def test_breweries_by_state(state):
    response = requests.get(f"{BASE_URL}?by_state={state}")
    assert response.status_code == 200
    Breweries.model_validate(response.json())

@pytest.mark.parametrize("brewery_id", ["madtree-brewing-cincinnati", "10-barrel-brewing-co-san-diego"])
def test_get_brewery_by_id(brewery_id):
    response = requests.get(f"{BASE_URL}/{brewery_id}")
    assert response.status_code == 200
    Brewery.model_validate(response.json())

@pytest.mark.parametrize("city, state", [
    ("san diego", "california"),
    ("austin", "texas")
])
def test_breweries_by_city(city, state):
    response = requests.get(
        BASE_URL,
        params={"by_city": city, "by_state": state}
    )
    assert response.status_code == 200
    Breweries.model_validate(response.json())

@pytest.mark.parametrize("brewery_type", ["micro", "regional", "brewpub"])
def test_breweries_by_type(brewery_type):
    response = requests.get(f"{BASE_URL}?by_type={brewery_type}")
    assert response.status_code == 200
    Breweries.model_validate(response.json())

def test_search_breweries():
    response = requests.get(f"{BASE_URL}/search?query=dog")
    assert response.status_code == 200
    Breweries.model_validate(response.json())