import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="class")
def login_data():
    return {"user": "a_test", "password": "a_test12345"}


@pytest.fixture(scope="class", autouse=True)
def setup_class(driver_init):
    pass
