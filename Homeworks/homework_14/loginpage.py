import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

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

    def check_current_tab(self):
        pass

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
        time.sleep(2)

    def get_modal_title_text(self, driver):
        modal_title_element = driver.find_element(*self.locators["btntitleloginonthetab"])
        return modal_title_element.text

    def test_current_tab_page(self, base_title, expected_title):
        actual_title = self.get_modal_title_text(self.driver)
        assert actual_title is not None, "Modal title element not found"
        assert actual_title == expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"

    def login(self, user, password):
        self.check_current_tab()
        time.sleep(10)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'logInModalLabel'))
        )
        self.user_name_field().send_keys(user)
        self.password_field().send_keys(password)

        time.sleep(10)
        self.login_button().click()
        time.sleep(80)
        try:
            WebDriverWait(self.driver, 60).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, 'loading-spinner-class'))

            )
        except TimeoutException:
            print("Timed out waiting for page to load after login")

    def wait_for_modal_to_disappear(self):
        try:
            WebDriverWait(self.driver, 20).until_not(
                EC.presence_of_element_located((By.CLASS_NAME, 'modal-backdrop'))
            )
        except TimeoutException:
            pass

    def test_welcome_text(self, base_test, expected_text):
        time.sleep(10)
        self.wait_for_modal_to_disappear()

        welcome_element = WebDriverWait(self.driver, 220).until(
            EC.visibility_of_element_located(self.locators["btntitleWelcometab"])
        )

        welcome_text = welcome_element.text
        assert expected_text.strip() == welcome_text.strip(), f"Expected text: '{expected_text}', Actual text: '{welcome_text}'"

    def test_Log_out_bt(self, base_bt_test, expected_bt_text):
        time.sleep(10)

        bt_element = WebDriverWait(self.driver, 220).until(
            EC.visibility_of_element_located(self.locators["btntitlelogouttab"])
        )

        btn_text = bt_element.text
        assert expected_bt_text.strip() == btn_text.strip(), f"Expected text: '{expected_bt_text}', Actual text: '{btn_text}'"
