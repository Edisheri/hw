import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAdminLoginPage:
    def test_login_form(self, browser, base_url):
        browser.get(f"{base_url}/administration")
        username = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "input-username"))
        )
        assert username.is_displayed()

    def test_password_field(self, browser, base_url):
        browser.get(f"{base_url}/administration")
        password = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "input-password"))
        )
        assert password.is_displayed()

    def test_login_button(self, browser, base_url):
        browser.get(f"{base_url}/administration")
        login_btn = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
        )
        assert login_btn.is_displayed()

    def test_login_form_header(self, browser, base_url):
        browser.get(f"{base_url}/administration")
        header = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".card-header"))
        )
        assert "Please enter your login details." in header.text

    def test_header_logo(self, browser, base_url):
        browser.get(f"{base_url}/administration")
        logo = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-brand"))
        )
        assert logo.is_displayed()