import pytest
import requests

@pytest.fixture
def test_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def expected_status(request):
    return request.config.getoption("--status_code")

def test_url_status_code(test_url, expected_status):
    response = requests.get(test_url)
    assert response.status_code == expected_status, (
        f"Ожидаемый код {expected_status}, "
        f"получен {response.status_code} для URL: {test_url}"
    )