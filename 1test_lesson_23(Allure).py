import allure
import pytest
from selenium import webdriver
from allure_commons.types import Severity
from allure_commons.types import AttachmentType


@pytest.mark.usefixture("driver_use")
@allure.epic("website")
@allure.feature("open_page")
@allure.story("get_website")
class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome()

    @pytest.mark.smoke
    @allure.title("Open login page")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://wiki.com/login", name="tz login")
    def test_open_login_page(self):
        with allure.step("Open login page.Step 1"):
            self.driver.get("https://demoqa.com/login")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="login page",
                attachment_type= allure.attachment_type.PNG
            )

        with allure.step("Open login page.Step 2"):
            assert self.driver.current_url == "https://demoqa.com/login", "Ошибка"

    @pytest.mark.regress
    @allure.title("Open books page")
    @allure.severity(Severity.CRITICAL)
    @allure.link(url="https://wiki.com/books", name="tz books")
    def test_open_books_page(self):
        with allure.step("Open books page.Step 1"):
            self.driver.get("https://demoqa.com/books")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="books page",
                attachment_type= allure.attachment_type.PNG
            )
        with allure.step("Open books page.Step 2"):
            assert self.driver.current_url == "https://demoqa.com/books", "Ошибка"

    @pytest.mark.integro
    @allure.title("Open profile page")
    @allure.severity(Severity.MINOR)
    @allure.link(url="https://wiki.com/profile", name="tz profile")
    def test_open_profile_page(self):
        with allure.step("Open profile page.Step 1"):
            self.driver.get("https://demoqa.com/profile")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="profile page",
                attachment_type= allure.attachment_type.PNG
            )
        with allure.step("Open profile page.Step 2"):
            assert self.driver.current_url == "https://demoqa.com/profile", "Ошибка"

    def teardown_method(self):
        self.driver.close()