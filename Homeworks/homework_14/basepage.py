
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
