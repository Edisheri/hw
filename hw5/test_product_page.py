import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestProductPage:
    def test_product_name(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=product/product&path=57&product_id=49")
        name = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        assert name.is_displayed()

    # Новый тест 2: Проверка наличия кнопки wishlist
    def test_product_price(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=product/product&path=57&product_id=49")
        price = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h2"))
        )
        assert price.is_displayed()
        assert "$" in price.text

    def test_add_to_cart_button(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=product/product&path=57&product_id=49")
        add_to_cart = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "button-cart"))
        )
        assert add_to_cart.is_displayed()

    def test_product_description(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=product/product&path=57&product_id=49")
        description = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#tab-description"))
        )
        assert description.is_displayed()

    def test_product_quantity(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=product/product&path=57&product_id=49")
        quantity = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "input-quantity"))
        )
        assert quantity.is_displayed()
        assert quantity.get_attribute("value") == "1"