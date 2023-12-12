from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import basepage
import locators
import loginpage
import time
from loginpage import LoginPage
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert


class CategoryPage(loginpage.LoginPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = locators.Locators.TEST_PAGE

    def category_monitors_button(self):
        return self.find_element(*self.locators["btncategory_monitors"])

    def click_monitor_button(self):
        # time.sleep(10)

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.locators["btncategory_monitors"])
        )
        self.category_monitors_button().click()

    def category_product_button(self):
        return self.find_element(*self.locators["btncategory_product"])

    def click_category_product_button(self):
        try:
            print("Before clicking the button")
            button = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.locators["btncategory_product"])
            )
            button.click()

            WebDriverWait(self.driver, 40).until(
                lambda driver: not button.is_enabled()
            )
            print("Button is stale")
        except StaleElementReferenceException as e:
            print(f"Element is stale - {e}")
        except TimeoutException as e:
            print(f"Timeout or element not found - {e}")

    def add_button(self):
        return self.find_element(*self.locators["btnadd"])

    def click_add_button(self):
        try:

            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.locators["btnadd"])
            )
            self.add_button().click()

            alert = WebDriverWait(self.driver, 50).until(EC.alert_is_present())
            alert.accept()

            time.sleep(5)

        except NoAlertPresentException:
            print("No Alert present")

    def cart_tab_button(self):
        return self.find_element(*self.locators["btnCartTab"])

    def click_cart_button(self):
        try:

            self.cart_tab_button().click()

            WebDriverWait(self.driver, 30).until(
                EC.url_to_be(locators.data.cartpage)
            )

            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(
                    (self.locators["imageCartTabe"])
                )
            )

            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.locators["ttlProductName"])
            )

            time.sleep(2)

        except TimeoutException:
            print("Timeout waiting for Cart button visibility")

    def get_product_name(self):

        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.locators["btntitleProductName"])
        )
        return self.find_element(*self.locators["btntitleProductName"]).text

    def get_product_price(self):

        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.locators["btntitleProductPrice"])
        )
        return self.find_element(*self.locators["btntitleProductPrice"]).text

    def test_cart_product(self):

        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.locators["ttlProductName"])
        )
        return self.find_element(*self.locators["ttlProductName"]).text

    def test_cart_product_price(self, expected_price):

        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.locators["ttlProductPrice"])
        )
        return self.find_element(*self.locators["ttlProductPrice"]).text
