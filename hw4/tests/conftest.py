import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="URL для проверки статус-кода"
    )
    parser.addoption(
        "--status_code",
        action="store",
        type=int,
        default=200,
        help="Ожидаемый HTTP статус-код"
    )

@pytest.fixture
def test_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def expected_status(request):
    return request.config.getoption("--status_code")