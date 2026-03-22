from selenium import webdriver


class TestExample:



    USERNAME_FIELD = ("xpath", "//input[@id='userName']")
    PASSWORD = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON = ("xpath", "//button[@id='login']")


    def setup_method(self):
       print("Предварительные условия")
       self.driver = webdriver.Chrome()

    def test_valid_data(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/login")

        username = driver.find_element(*self.USERNAME_FIELD)
        username.send_keys("Alexei")
        assert username.get_attribute("value") == "Alexei"

        password = driver.find_element(*self.PASSWORD)
        password.send_keys("qwerty")
        assert password.get_attribute("value") == "qwerty"

        driver.find_element(*self.LOGIN_BUTTON).click()

    def teardown_method(self):
        print("Финальные условия")
        self.driver.quit()




