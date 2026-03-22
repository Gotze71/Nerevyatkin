import pytest
import os
from collections import namedtuple
from faker import Faker
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
faker = Faker()

@pytest.fixture()
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    request.cls.FIRST_NAME = faker.first_name()
    request.cls.LAST_NAME = faker.last_name()
    request.cls.ZIP = faker.zipcode()
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def setup_environment_properties():
    properties = {
        "STAGE": os.environ["STAGE"],
        "BROWSER": os.environ["BROWSER"],
        "PYTHON": os.environ["PYTHON"],
        "MR": os.environ["MR"]
        }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")