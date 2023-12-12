from selenium.webdriver.common.by import By


class Locators:
    TEST_PAGE = {
        "btntitleloginonthetab": (By.ID, 'logInModalLabel'),
        "btnloginonthetab": (By.ID, 'login2'),
        "edtusername": (By.ID, 'loginusername'),
        "edtpassword": (By.ID, 'loginpassword'),
        "btnsignin": (
            By.XPATH, "//button[@type='button' and contains(@onclick, 'logIn') and contains(@class, 'btn-primary')]"),
        "btntitlelogouttab": (By.ID, 'logout2'),
        "btntitleWelcometab": (By.ID, 'nameofuser'),
        "btncategory_monitors": (By.XPATH, '//a[@onclick="byCat(\'monitor\')"]'),
        "btncategory_product": (By.XPATH, '//a[@href="prod.html?idp_=10" and contains(@class, "hrefch")]'),
        "btntitleProductName": (By.XPATH, '//*[@id="tbodyid"]/h2'),
        "btntitleProductPrice": (By.CLASS_NAME, "price-container"),
        "btnadd": (By.XPATH, '//a[contains(@onclick, "addToCart(10)")]'),
        "btnCartTab": (By.ID, 'cartur'),
        "ttlProductName": (By.XPATH, "//td[text()='Apple monitor 24']"),
        "ttlProductPrice": (By.XPATH, "//td[text()='400']"),
        "imageCartTabe": (By.XPATH, '//img[@width="100" and @height="100" and @src="imgs/apple_cinema.jpg"]')

    }


class data:
    base_url = "https://www.demoblaze.com/"
    cartpage = "https://www.demoblaze.com/cart.html"