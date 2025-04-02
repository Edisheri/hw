import pytest
import requests

@pytest.fixture
def test_params(request):
    return {
        "url": request.config.getoption("--url"),
        "status_code": request.config.getoption("--status_code")
    }

def test_custom_url_status_code(test_params):
    response = requests.get(test_params["url"])
    assert response.status_code == test_params["status_code"], (
        f"Ожидался статус {test_params['status_code']}, "
        f"получен {response.status_code} для URL: {test_params['url']}"
    )