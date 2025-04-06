import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCatalogPage:
    def test_category_title(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=product/category&path=20")
        title = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h2"))
        )
        assert "Desktops" in title.text

    def test_sort_dropdown(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=product/category&path=20")
        sort = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "input-sort"))
        )
        assert sort.is_displayed()
        assert "Default" in sort.text

    def test_pagination(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=product/category&path=20")
        pagination = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".pagination"))
        )
        assert pagination.is_displayed()
        assert "1" in pagination.text

    def test_product_thumbnails(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=product/category&path=20")
        thumbnails = WebDriverWait(browser, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-thumb"))
        )
        assert len(thumbnails) > 0, "No product thumbnails found"

    def test_product_price(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=product/category&path=20")
        price = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".price"))
        )
        assert price.is_displayed()
        assert "$" in price.text