import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHomePage:
    def test_logo(self, browser, base_url):
        browser.get(base_url)
        logo = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "logo"))
        )
        assert logo.is_displayed()

    def test_search_field(self, browser, base_url):
        browser.get(base_url)
        search = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.NAME, "search"))
        )
        assert search.is_displayed()

    def test_cart_link(self, browser, base_url):
        browser.get(base_url)
        cart_link = WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//a[contains(@href, 'route=checkout/cart')]")
            )
        )
        assert cart_link.is_displayed()
        assert "Shopping Cart" in cart_link.text

    def test_menu_categories(self, browser, base_url):
        browser.get(base_url)
        menu = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "menu"))
        )
        assert menu.is_displayed()

    def test_featured_products(self, browser, base_url):
        browser.get(base_url)
        featured_products = WebDriverWait(browser, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-thumb"))
        )
        assert len(featured_products) >= 4, "Недостаточно рекомендуемых товаров"