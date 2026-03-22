from tkinter.constants import CURRENT

import allure
import pytest
import time
from selenium.webdriver.support.select import Select
from allure_commons.types import Severity
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"
LOGIN = "user_login"
PASSWORD = "secret_sauce"


@allure.epic("Base User Steps")
@allure.feature("Authorization, Buy, Logout")
@allure.story("Buy Fleece Jacket")
@pytest.mark.usefixtures("driver")
class TestBuySelectedProduct:

    @pytest.mark.regression
    @allure.title("Покупка выбранного товара авторизованным пользователем")
    @allure.severity(Severity.CRITICAL)
    @allure.link(url="https://www.wiki.com/saucedemo", name="Документация проекта")
    def test_login_buy(self):
        with allure.step("Открытие страницы https://www.saucedemo.com/"):
            self.driver.get(URL)
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Страница авторизации",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Проверка корректности URL: https://www.saucedemo.com/"):
            assert self.driver.current_url == URL, "405 Error in URL"


        with allure.step("Проверка поля логин"):
            USER_NAME = self.driver.find_element("xpath", "//input[@id = 'user-name']")
            USER_NAME.clear()
            assert USER_NAME.get_attribute("value") == "", "403 Error in USER_NAME"
        with allure.step("Ввод данных в поле логин"):
            USER_NAME.send_keys("standard_user")
            time.sleep(1)
        with allure.step("Проверка корректности введенных данных в поле логин"):
            USER_NAME.get_attribute("value")
            assert USER_NAME.get_attribute("value") == "standard_user", "404 Error in USER_NAME"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка корректности введенных данных в поле логин",
                attachment_type=allure.attachment_type.PNG
            )


        with allure.step("Проверка поля пароль"):
            PASSWORD = self.driver.find_element("xpath", "//input[@id = 'password']")
            PASSWORD.clear()
            assert PASSWORD.get_attribute("value") == "", "403 Error in PASSWORD"
        with allure.step("Ввод данных в поле пароль"):
            PASSWORD.send_keys("secret_sauce")
            time.sleep(1)
        with allure.step("Проверка корректности введенных данных в поле пароль"):
            PASSWORD.get_attribute("value")
            assert PASSWORD.get_attribute("value") == "secret_sauce", "403 Error in PASSWORD"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка корректности введенных данных в поле пароль",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Поиск и нажатие кнопки [Login]"):
            LOGIN_BUTTON = ("xpath", "//input[@id = 'login-button']")
            self.driver.find_element(*LOGIN_BUTTON).click()
            time.sleep(1)

        with allure.step("Проверка корректности перехода на страницу 'https://www.saucedemo.com/inventory.html'"):
            CURRENT_URL_INVENTORY = self.driver.current_url
            URL_INVENTORY = "https://www.saucedemo.com/inventory.html"
            assert CURRENT_URL_INVENTORY == URL_INVENTORY, "405 Error in URL_INVENTORY"
            time.sleep(1)
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка корректности перехода на страницу 'https://www.saucedemo.com/inventory.html'",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Переход на страницу 'Информация о товаре' для товар3"):
            T_SHIRT = self.driver.find_element("xpath", "//a[@id = 'item_3_title_link']")
            T_SHIRT.click()
            time.sleep(1)
        with allure.step("Проверка корректности перехода на страницу 'https://www.saucedemo.com/inventory-item.html?id=3'"):
            T_SHIRT_CURRENT_URL = self.driver.current_url
            T_SHIRT_URL = "https://www.saucedemo.com/inventory-item.html?id=3"
            assert T_SHIRT_CURRENT_URL == T_SHIRT_URL, "405 Error in T_SHIRT_URL"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка корректности перехода на страницу 'https://www.saucedemo.com/inventory-item.html?id=3'",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Открытие бургера страницы"):
            BURGER = self.driver.find_element("xpath", "//button[@id = 'react-burger-menu-btn']")
            BURGER.click()
            time.sleep(1)
        with allure.step("Переход на страницу всех товаров через бургер"):
            ALL_ITEMS_BUTTON = self.driver.find_element("xpath", "//A[@id = 'inventory_sidebar_link']")
            ALL_ITEMS_BUTTON.click()
            time.sleep(1)
        with allure.step("Проверка корректности перехода на страницу 'https://www.saucedemo.com/inventory.html'"):
            assert CURRENT_URL_INVENTORY == URL_INVENTORY, "406 Error in URL_INVENTORY"
            time.sleep(1)
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка корректности перехода на страницу 'https://www.saucedemo.com/inventory.html'",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Сортировка товаров на странице A-Z"):
            DROPDOWN_A_Z = self.driver.find_element("xpath", "//select[@class = 'product_sort_container']")
            DROPDOWN = Select(DROPDOWN_A_Z)
            DROPDOWN.select_by_value("za")
            time.sleep(1)
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Товары отсортированы на странице A-Z",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Добавление в корзину товар5"):
            ADD_TO_CART_JACKET_BUTTON = self.driver.find_element("xpath","//button[@id = 'add-to-cart-sauce-labs-fleece-jacket']")
            ADD_TO_CART_JACKET_BUTTON.click()
            time.sleep(1)
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Товар5 добавлен в корзину",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Переход на страницу 'Корзина'"):
            SHOP_BASKET_BUTTON = self.driver.find_element("xpath", "//A[@class = 'shopping_cart_link']")
            SHOP_BASKET_BUTTON.click()
            time.sleep(1)
        with allure.step("Проверка корректности перехода на страницу 'https://www.saucedemo.com/cart.html'"):
            SHOP_BASKET_CURRENT_URL = self.driver.current_url
            SHOP_BASKET_URL = "https://www.saucedemo.com/cart.html"
            assert SHOP_BASKET_CURRENT_URL == SHOP_BASKET_URL, "405 Error in SHOP_BASKET_URL"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка корректности перехода на страницу 'https://www.saucedemo.com/cart.html'",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Проверка товар5 в корзине"):
            JACKET_IN_BASKET = self.driver.find_element("xpath", "//a[@id='item_5_title_link']")
            JACKET_ID = JACKET_IN_BASKET.get_attribute("id")
            assert JACKET_ID == 'item_5_title_link', "405 Error in JACKET_ID"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка товар5 в корзине",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Поиск и нажатие кнопки [Checkout]"):
            CHECKOUT_BUTTON = self.driver.find_element("xpath", "//button[@id = 'checkout']")
            CHECKOUT_BUTTON.click()
            time.sleep(1)

        with allure.step("Проверка корректности перехода на страницу 'https://www.saucedemo.com/checkout-step-one.html'"):
            CHECKOUT_PAGE_CURRENT_URL = self.driver.current_url
            CHECKOUT_PAGE_URL = "https://www.saucedemo.com/checkout-step-one.html"
            assert CHECKOUT_PAGE_CURRENT_URL == CHECKOUT_PAGE_URL, "405 Error in CHECKOUT_PAGE_URL"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка корректности перехода на страницу 'https://www.saucedemo.com/checkout-step-one.html'",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Проверка поля имя"):
            FIRST_NAME = self.driver.find_element("xpath", "//input[@id = 'first-name']")
            FIRST_NAME.clear()
            assert FIRST_NAME.get_attribute("value") == "", "403 Error in FIRST_NAME"
        with allure.step("Ввод данных в поле имя"):
            FIRST_NAME.send_keys(self.FIRST_NAME)
            time.sleep(1)
        with allure.step("Проверка корректности введенных данных в поле имя"):
            FIRST_NAME.get_attribute("value")
            assert FIRST_NAME.get_attribute("value") == self.FIRST_NAME, "404 Error in FIRST_NAME"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка корректности введенных данных в поле имя",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Проверка поля фамилия"):
            LAST_NAME = self.driver.find_element("xpath", "//input[@id = 'last-name']")
            LAST_NAME.clear()
            assert LAST_NAME.get_attribute("value") == "", "403 Error in LAST_NAME"
        with allure.step("Ввод данных в поле фамилия"):
            LAST_NAME.send_keys(self.LAST_NAME)
            time.sleep(1)
        with allure.step("Проверка корректности введенных данных в поле фамилия"):
            LAST_NAME.get_attribute("value")
            assert LAST_NAME.get_attribute("value") == self.LAST_NAME, "404 Error in LAST_NAME"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка корректности введенных данных в поле фамилия",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Проверка поля индекс"):
            ZIP = self.driver.find_element("xpath", "//input[@id = 'postal-code']")
            ZIP.clear()
            assert ZIP.get_attribute("value") == "", "403 Error in ZIP"
        with allure.step("Ввод данных в поле индекс"):
            ZIP.send_keys(self.ZIP)
            time.sleep(1)
        with allure.step("Проверка корректности введенных данных в поле индекс"):
            ZIP.get_attribute("value")
            assert ZIP.get_attribute("value") == self.ZIP, "404 Error in ZIP"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка корректности введенных данных в поле индекс",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Поиск и нажатие кнопки [Continue]"):
            CONTINUE_BUTTON = self.driver.find_element("xpath", "//input[@id = 'continue']")
            CONTINUE_BUTTON.click()
            time.sleep(1)

        with allure.step("Проверка корректности перехода на страницу 'https://www.saucedemo.com/checkout-step-two.html'"):
            CHECKOUT_PAGE2_CURRENT_URL = self.driver.current_url
            CHECKOUT_PAGE2_URL = "https://www.saucedemo.com/checkout-step-two.html"
            assert CHECKOUT_PAGE2_CURRENT_URL == CHECKOUT_PAGE2_URL, "405 Error in CHECKOUT_PAGE2_URL"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка корректности перехода на страницу 'https://www.saucedemo.com/checkout-step-two.html'",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Проверка товар5 в чеке"):
            JACKET_IN_CHECK = self.driver.find_element("xpath", "//a[@id='item_5_title_link']")
            JACKET_ID = JACKET_IN_CHECK.get_attribute("id")
            assert JACKET_ID == 'item_5_title_link', "405 Error in JACKET_ID"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка товар5 в чеке",
                attachment_type=allure.attachment_type.PNG
            )
        with allure.step("Поиск и нажатие кнопки [Finish]"):
            FINISH_BUTTON = self.driver.find_element("xpath", "//button[@id = 'finish']")
            FINISH_BUTTON.click()
            time.sleep(1)

        with allure.step(
            "Проверка корректности перехода на страницу 'https://www.saucedemo.com/checkout-complete.html'"):
            CHECKOUT_COMPLETE_PAGE_URL = self.driver.current_url
            CHECKOUT_COMPLETE_PAGE = "https://www.saucedemo.com/checkout-complete.html"
            assert CHECKOUT_COMPLETE_PAGE_URL == CHECKOUT_COMPLETE_PAGE, "405 Error in CHECKOUT_COMPLETE_PAGE"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка корректности перехода на страницу 'https://www.saucedemo.com/checkout-complete.html'",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Поиск и нажатие кнопки [Back Home]"):
            BACK_HOME_BUTTON = self.driver.find_element("xpath", "//button[@id = 'back-to-products']")
            BACK_HOME_BUTTON.click()
            time.sleep(1)

        with allure.step("Проверка корректности перехода на страницу 'https://www.saucedemo.com/inventory.html'"):
            assert self.driver.current_url == URL_INVENTORY, "407 Error in URL"
            time.sleep(1)
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Проверка корректности перехода на страницу 'https://www.saucedemo.com/inventory.html'",
                attachment_type=allure.attachment_type.PNG
            )