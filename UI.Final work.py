import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com")
CURRENT_URL = driver.current_url
URL = "https://www.saucedemo.com/"
assert CURRENT_URL == URL, "405 Error in URL"

USER_NAME = driver.find_element("xpath", "//input[@id = 'user-name']")
USER_NAME.clear()
assert USER_NAME.get_attribute("value") == "", "403 Error in USER_NAME"
USER_NAME.send_keys("standard_user")
time.sleep(1)
USER_NAME.get_attribute("value")
assert USER_NAME.get_attribute("value") == "standard_user" , "404 Error in USER_NAME"

PASSWORD = driver.find_element("xpath", "//input[@id = 'password']")
PASSWORD.clear()
assert PASSWORD.get_attribute("value") == "", "403 Error in PASSWORD"
PASSWORD.send_keys("secret_sauce")
time.sleep(1)
PASSWORD.get_attribute("value")
assert PASSWORD.get_attribute("value") == "secret_sauce" , "404 Error in PASSWORD"

LOGIN_BUTTON = ("xpath", "//input[@id = 'login-button']")
driver.find_element(*LOGIN_BUTTON).click()
time.sleep(1)

CURRENT_URL_INVENTORY = driver.current_url
URL_INVENTORY = "https://www.saucedemo.com/inventory.html"
assert CURRENT_URL_INVENTORY == URL_INVENTORY, "405 Error in URL_INVENTORY"
time.sleep(1)

T_SHIRT = driver.find_element("xpath", "//a[@id = 'item_3_title_link']")
T_SHIRT.click()
time.sleep(1)

T_SHIRT_CURRENT_URL = driver.current_url
T_SHIRT_URL = "https://www.saucedemo.com/inventory-item.html?id=3"
assert T_SHIRT_CURRENT_URL == T_SHIRT_URL, "405 Error in T_SHIRT_URL"

BURGER = driver.find_element("xpath", "//button[@id = 'react-burger-menu-btn']")
BURGER.click()
time.sleep(1)

ALL_ITEMS_BUTTON = driver.find_element("xpath", "//A[@id = 'inventory_sidebar_link']")
ALL_ITEMS_BUTTON.click()
time.sleep(1)

assert CURRENT_URL_INVENTORY == URL_INVENTORY, "406 Error in URL_INVENTORY"
time.sleep(1)

DROPDOWN_A_Z = driver.find_element("xpath", "//select[@class = 'product_sort_container']")
DROPDOWN = Select(DROPDOWN_A_Z)
DROPDOWN.select_by_value("za")
time.sleep(1)

ADD_TO_CART_JACKET_BUTTON = driver.find_element("xpath", "//button[@id = 'add-to-cart-sauce-labs-fleece-jacket']")
ADD_TO_CART_JACKET_BUTTON.click()
time.sleep(1)

SHOP_BASKET_BUTTON = driver.find_element("xpath", "//A[@class = 'shopping_cart_link']")
SHOP_BASKET_BUTTON.click()
time.sleep(1)

SHOP_BASKET_CURRENT_URL = driver.current_url
SHOP_BASKET_URL = "https://www.saucedemo.com/cart.html"
assert SHOP_BASKET_CURRENT_URL == SHOP_BASKET_URL, "405 Error in SHOP_BASKET_URL"

JACKET_IN_BASKET = driver.find_element("xpath", "//a[@id='item_5_title_link']")
JACKET_ID = JACKET_IN_BASKET.get_attribute("id")
assert JACKET_ID == 'item_5_title_link', "405 Error in JACKET_ID"

CHECKOUT_BUTTON = driver.find_element("xpath", "//button[@id = 'checkout']")
CHECKOUT_BUTTON.click()
time.sleep(1)

CHECKOUT_PAGE_CURRENT_URL = driver.current_url
CHECKOUT_PAGE_URL = "https://www.saucedemo.com/checkout-step-one.html"
assert CHECKOUT_PAGE_CURRENT_URL == CHECKOUT_PAGE_URL, "405 Error in CHECKOUT_PAGE_URL"

FIRST_NAME = driver.find_element("xpath", "//input[@id = 'first-name']")
FIRST_NAME.clear()
assert FIRST_NAME.get_attribute("value") == "", "403 Error in FIRST_NAME"
FIRST_NAME.send_keys("Aleksei")
time.sleep(1)
FIRST_NAME.get_attribute("value")
assert FIRST_NAME.get_attribute("value") == "Aleksei" , "404 Error in FIRST_NAME"

LAST_NAME = driver.find_element("xpath", "//input[@id = 'last-name']")
LAST_NAME.clear()
assert LAST_NAME.get_attribute("value") == "", "403 Error in LAST_NAME"
LAST_NAME.send_keys("Nerevyatkin")
time.sleep(1)
LAST_NAME.get_attribute("value")
assert LAST_NAME.get_attribute("value") == "Nerevyatkin" , "404 Error in LAST_NAME"

ZIP = driver.find_element("xpath", "//input[@id = 'postal-code']")
ZIP.clear()
assert ZIP.get_attribute("value") == "", "403 Error in ZIP"
ZIP.send_keys("717171")
time.sleep(1)
ZIP.get_attribute("value")
assert ZIP.get_attribute("value") == "717171" , "404 Error in ZIP"

CONTINUE_BUTTON = driver.find_element("xpath", "//input[@id = 'continue']")
CONTINUE_BUTTON.click()
time.sleep(1)

CHECKOUT_PAGE2_CURRENT_URL = driver.current_url
CHECKOUT_PAGE2_URL = "https://www.saucedemo.com/checkout-step-two.html"
assert CHECKOUT_PAGE2_CURRENT_URL == CHECKOUT_PAGE2_URL, "405 Error in CHECKOUT_PAGE2_URL"

JACKET_IN_CHECK = driver.find_element("xpath", "//a[@id='item_5_title_link']")
JACKET_ID = JACKET_IN_CHECK.get_attribute("id")
assert JACKET_ID == 'item_5_title_link', "405 Error in JACKET_ID"

FINISH_BUTTON = driver.find_element("xpath", "//button[@id = 'finish']")
FINISH_BUTTON.click()
time.sleep(1)

CHECKOUT_COMPLETE_PAGE_URL = driver.current_url
CHECKOUT_COMPLETE_PAGE = "https://www.saucedemo.com/checkout-complete.html"
assert CHECKOUT_COMPLETE_PAGE_URL == CHECKOUT_COMPLETE_PAGE, "405 Error in CHECKOUT_COMPLETE_PAGE"

BACK_HOME_BUTTON = driver.find_element("xpath", "//button[@id = 'back-to-products']")
BACK_HOME_BUTTON.click()
time.sleep(1)

assert CURRENT_URL == URL, "407 Error in URL"

driver.quit()