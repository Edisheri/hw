import pytest
import requests

def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru")
    parser.addoption("--status_code", default=200, type=int)

@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")

def test_url_status_code(url, status_code):
    try:
        response = requests.get(url, timeout=10)
        assert response.status_code == status_code
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {str(e)}")