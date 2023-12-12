from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import basepage
import locators


class LoginPage(basepage.BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = locators.Locators.TEST_PAGE

    def tab_login_button(self):
        return self.find_element(*self.locators["btnloginonthetab"])

    def user_name_field(self):
        return self.find_element(*self.locators["edtusername"])

    def password_field(self):
        return self.find_element(*self.locators["edtpassword"])

    def login_button(self):
        return self.find_element(*self.locators["btnsignin"])

    def open_tab_page(self):
        self.tab_login_button().click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.locators["btntitleloginonthetab"])
        )

    def login(self, user, password):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'logInModalLabel'))
        )

        username_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'loginusername'))
        )
        username_field.send_keys(user)

        password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'loginpassword'))
        )
        password_field.send_keys(password)

    def click_on_login_btn(self):
        self.login_button().click()
        time.sleep(10)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, 'loading-spinner-class'))

            )
        except TimeoutException:
            print("Timed out waiting for page to load after login")

    def is_element_displayed(self, locator):
        try:
            return WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    def is_login_page_username_displayed(self):
        return self.is_element_displayed(self.locators["edtusername"])

    def is_login_page_password_displayed(self):
        return self.is_element_displayed(self.locators["edtpassword"])

    def get_welcome_text(self):
        return self.find_element(*self.locators["btntitleWelcometab"]).text

    def get_logout_button_text(self):
        return self.find_element(*self.locators["btntitlelogouttab"]).text

