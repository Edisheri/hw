import pytest

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="URL для тестирования")
    parser.addoption("--status_code", action="store", default=200, type=int, help="Ожидаемый HTTP статус код")