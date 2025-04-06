import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrationPage:
    def test_firstname_field(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=account/register")
        firstname = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "input-firstname"))
        )
        assert firstname.is_displayed()

    def test_lastname_field(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=account/register")
        lastname = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "input-lastname"))
        )
        assert lastname.is_displayed()

    def test_email_field(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=account/register")
        email = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "input-email"))
        )
        assert email.is_displayed()

    def test_password_field(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=account/register")
        password = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "input-password"))
        )
        assert password.is_displayed()

    def test_submit_button(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=account/register")
        submit_btn = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
            )
        )
        assert submit_btn.is_displayed()
        assert "Continue" in submit_btn.text
        assert "btn-primary" in submit_btn.get_attribute("class")