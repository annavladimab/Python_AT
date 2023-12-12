from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def check_current_url(self, expected_url):
        assert self.get_url() == expected_url, f"Expected URL: {expected_url}, Actual URL: {self.get_url()}"

    def open_page(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def wait_for_page_to_load(self):

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//a[@href="prod.html?idp_=1" and @class="hrefch"]')
                )
            )
        except TimeoutException:
            print("Page did not load within the specified time.")
