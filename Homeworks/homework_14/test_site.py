import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException

import fixture
from fixture import driver_init, login_data, setup, category_setup


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login_scenario(self, login_data):
        self.login_page.open_tab_page()
        assert self.login_page.is_login_page_username_displayed()
        assert self.login_page.is_login_page_password_displayed()
        self.login_page.login(user=login_data["user"], password=login_data["password"])
        self.login_page.click_on_login_btn()
        assert "Log out" in self.login_page.get_logout_button_text().strip()
        assert "Welcome a_test" in self.login_page.get_welcome_text().strip()


@pytest.mark.usefixtures("setup", "category_setup")
class TestCategory:

    def test_product_name_and_price(self):
        self.category_page.click_monitor_button()
        self.category_page.click_category_product_button()

        expected_product_name = "Apple monitor 24"
        assert expected_product_name in self.category_page.get_product_name().strip()

        expected_product_price = "$400 *includes tax"
        assert expected_product_price in self.category_page.get_product_price().strip()

       # def test_added_product_name_and_price(self):
        self.category_page.click_add_button()
        self.category_page.click_cart_button()

        expected_product_name = "Apple monitor 24"
        assert expected_product_name in self.category_page.test_cart_product().strip()

        expected_cart_product_price = 400
        assert self.category_page.test_cart_product_price(expected_cart_product_price)
