import pytest
from selenium import webdriver

import basepage
import loginpage
import categorypage
import locators


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="class", autouse=True)
def setup(request, driver_init):
    driver = driver_init
    request.cls.login_page = loginpage.LoginPage(driver)
    request.cls.category_page = categorypage.CategoryPage(driver)

    base_url = locators.data.base_url
    base_page = basepage.BasePage(driver)
    base_page.open_page(base_url)
    base_page.wait_for_page_to_load()


@pytest.fixture(scope="class")
def login_data():
    return {"user": "a_test", "password": "a_test12345"}


@pytest.fixture(scope="class")
def category_setup(request, setup, login_data):
    request.cls.login_page.open_tab_page()
    request.cls.login_page.login(user=login_data["user"], password=login_data["password"])
    request.cls.login_page.click_on_login_btn()
