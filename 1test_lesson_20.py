import pytest
from selenium import webdriver

class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome()
    @pytest.mark.smoke
    def test_open_login_page(self):
        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://demoqa.com/login", "Ошибка"
    @pytest.mark.regress
    def test_open_books_page(self):
        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "https://demoqa.com/books", "Ошибка"
    @pytest.mark.integro
    def test_open_profile_page(self):
        self.driver.get("https://demoqa.com/profile")
        assert self.driver.current_url == "https://", "Ошибка"

    def teardown_method(self):
        self.driver.close()