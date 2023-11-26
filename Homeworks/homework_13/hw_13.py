import unittest
from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "edtUserName": ('name', 'user-name'),
        "edtPassword": ('id', 'password'),
        "btnSignIn": ('XPATH', '//input[@value="Login"]')
    }

    def login(self):

        self.edtUserName.set_text("standard_user")
        self.edtPassword.set_text("secret_sauce")
        self.btnSignIn.click_button()

    def check_current_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url


class LoginTest(unittest.TestCase):

    def test_Login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")

        pglogin = LoginPage(driver)
        pglogin.login()

        expected_url = 'https://www.saucedemo.com/inventory.html'

        pglogin.check_current_url(expected_url)


if __name__ == "__main__":
    unittest.main()
