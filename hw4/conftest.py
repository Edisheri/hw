import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="URL для проверки статус кода"
    )
    parser.addoption(
        "--status_code",
        action="store",
        default=200,
        type=int,
        help="Ожидаемый HTTP статус код"
    )

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def expected_status_code(request):
    return request.config.getoption("--status_code")