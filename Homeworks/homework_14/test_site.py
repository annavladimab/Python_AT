import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException

import basepage
import loginpage
import categorypage
from fixture import driver_init, login_data, setup_class


class BaseTest:

    @classmethod
    def setup_class(cls):
        cls.login_page = loginpage.LoginPage(cls.driver)
        cls.category_page = categorypage.CategoryPage(cls.driver)

    @pytest.mark.parametrize("base_url, expected_url", [("https://www.demoblaze.com/", "https://www.demoblaze.com/")])
    def test_base_page_url(self, base_url, expected_url):
        base_page = basepage.BasePage(self.driver)
        base_page.open_page(base_url)
        base_page.check_current_url(expected_url)


class TestLogin(BaseTest):

    @pytest.mark.parametrize("base_url, expected_url", [("https://www.demoblaze.com/", "https://www.demoblaze.com/")])
    def test_login_page_url(self, base_url, expected_url):
        self.login_page.open_tab_page()

    @pytest.mark.parametrize("base_title, expected_title", [("Log in", "Log in")])
    def test_current_tab_page(self, base_title, expected_title):
        self.login_page.test_current_tab_page(base_title, expected_title)

    @pytest.mark.usefixtures("driver_init", "login_data")
    def test_login_page(self, login_data):
        self.login_page.login(**login_data)

    @pytest.mark.parametrize("base_w_text, expected_w_text", [("Welcome a_test", "Welcome a_test")])
    def test_welcome_text(self, base_w_text, expected_w_text):
        self.login_page.test_welcome_text(base_w_text, expected_w_text)


class TestCategory(TestLogin):

    @pytest.mark.parametrize("base_url, expected_url", [("https://www.demoblaze.com/", "https://www.demoblaze.com/")])
    def test_category_url(self, base_url, expected_url):
        try:
            self.category_page.click_monitor_button()
        except NoSuchElementException as e:
            self.fail(f"Element not found - {e}")

    @pytest.mark.parametrize("base_url, expected_url", [
        ("https://www.demoblaze.com/prod.html?idp_=10", "https://www.demoblaze.com/prod.html?idp_=10")])
    def test_product_url(self, base_url, expected_url):
        self.category_page.click_category_product_button()

    @pytest.mark.parametrize("product_name, expected_product_name", [("Apple monitor 24", "Apple monitor 24")])
    def test_product_name(self, product_name, expected_product_name):
        # self.category_page.click_category_product_button()
        self.category_page.test_product_name(product_name, expected_product_name)

    @pytest.mark.parametrize("product_price, expected_product_price", [("$400 *includes tax", "$400 *includes tax")])
    def test_product_price(self, product_price, expected_product_price):
        self.category_page.test_product_price(product_price, expected_product_price)
        self.category_page.click_add_button()

    @pytest.mark.parametrize("cart_product_name, expected_cart_product_name",
                             [("Apple monitor 24", "Apple monitor 24")])
    def test_cart_product(self, cart_product_name, expected_cart_product_name):
        self.category_page.click_cart_button()
        self.category_page.test_cart_product(cart_product_name, expected_cart_product_name)

    @pytest.mark.parametrize("cart_product_price, expected_cart_product_price", [("400", "400")])
    def test_cart_product_price(self, cart_product_price, expected_cart_product_price):
        self.category_page.test_cart_product_price(cart_product_price, expected_cart_product_price)
