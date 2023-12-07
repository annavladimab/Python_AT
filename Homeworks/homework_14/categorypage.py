import time

from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import basepage
import locators
import loginpage

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
        self.category_monitors_button().click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.locators["btncategory_monitors"])
        )
        time.sleep(20)

    def category_product_button(self):
        return self.find_element(*self.locators["btncategory_product"])

    def click_category_product_button(self):
        try:
            print("Before clicking the button")
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators["btncategory_product"])
            )
            print("Button is clickable")
            button.click()
            print("Button clicked")

            WebDriverWait(self.driver, 20).until(
                lambda driver: not button.is_enabled()
            )
            print("Button is stale")
        except StaleElementReferenceException as e:
            print(f"Element is stale - {e}")
        except TimeoutException as e:
            print(f"Timeout or element not found - {e}")

    def wait_for_modal_to_disappear(self):
        try:
            WebDriverWait(self.driver, 20).until_not(
                EC.presence_of_element_located((By.CLASS_NAME, 'modal-backdrop'))
            )
        except TimeoutException:
            pass

    def test_product_name(self, product_name, expected_product_name):
        time.sleep(110)
        self.wait_for_modal_to_disappear()

        product_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.locators["btntitleProductName"])
        )

        product_text = product_element.text
        assert expected_product_name.strip() == product_text.strip(), f"Expected text: '{expected_product_name}', Actual text: '{product_text}'"

    def test_product_price(self, product_price, expected_product_price):
        time.sleep(110)
        self.wait_for_modal_to_disappear()

        product_price_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.locators["btntitleProductPrice"])
        )

        product_price_text = product_price_element.text
        assert expected_product_price == product_price_text, f"Expected text: '{expected_product_price}', Actual text: '{product_price_text}'"

    def add_button(self):
        return self.find_element(*self.locators["btnadd"])

    def click_add_button(self):
        try:

            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.locators["btnadd"])
            )
            self.add_button().click()

            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert.accept()

            time.sleep(20)

        except NoAlertPresentException:
            print("No Alert present")

    def cart_tab_button(self):
        return self.find_element(*self.locators["btnCartTab"])

    def click_cart_button(self):
        try:

            print("Before waiting for visibility of Cart button")
            print(f"Current URL: {self.driver.current_url}")

            self.cart_tab_button().click()

            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.locators["btnCartTab"])
            )

            time.sleep(2)

        except TimeoutException:
            print("Timeout waiting for Cart button visibility")

    def test_cart_product(self, cart_product_name, expected_cart_product_name):

        time.sleep(110)
        self.wait_for_modal_to_disappear()

        cart_product_element = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.locators["ttlProductName"])
        )

        cart_product_text = cart_product_element.text
        assert expected_cart_product_name.strip() == cart_product_text.strip(), f"Expected text: '{expected_cart_product_name}', Actual text: '{cart_product_text}'"
        time.sleep(110)

    def test_cart_product_price(self, cart_product_price, expected_cart_product_price):

        time.sleep(110)
        self.wait_for_modal_to_disappear()

        cart_product_price_element = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.locators["ttlProductPrice"])
        )

        cart_product_price_text = cart_product_price_element.text
        assert expected_cart_product_price.strip() == cart_product_price_text.strip(), f"Expected text: '{expected_cart_product_price}', Actual text: '{cart_product_price_text}'"
        time.sleep(110)
