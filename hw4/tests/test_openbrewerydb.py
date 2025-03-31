import pytest
import requests
from hw4.tests.models import Brewery

BASE_URL = "https://api.openbrewerydb.org/v1/breweries"

@pytest.mark.parametrize("state", ["new_york", "california", "texas"])
def test_breweries_by_state(state):
    response = requests.get(f"{BASE_URL}?by_state={state}")
    assert response.status_code == 200
    breweries = response.json()
    for brewery in breweries:
        Brewery(**brewery)

def test_get_brewery_by_id():
    search_response = requests.get(f"{BASE_URL}?by_name=madtree")
    assert search_response.status_code == 200
    breweries = search_response.json()
    assert len(breweries) > 0

    valid_id = breweries[0]["id"]
    response = requests.get(f"{BASE_URL}/{valid_id}")
    assert response.status_code == 200
    Brewery(**response.json())

@pytest.mark.parametrize("city, state", [
    ("san_diego", "california"),
    ("austin", "texas")
])
def test_breweries_by_city(city, state):
    response = requests.get(f"{BASE_URL}?by_city={city}&by_state={state}")
    assert response.status_code == 200
    breweries = response.json()
    for brewery in breweries:
        Brewery(**brewery)