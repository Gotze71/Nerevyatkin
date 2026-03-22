import pytest
import os
from collections import namedtuple
from faker import Faker
from selenium import webdriver
faker = Faker()

@pytest.fixture
def  user():

        login = faker.user_name()
        password = faker.password()
        User = namedtuple("_", ["login", "password"])
        return User(login, password)

@pytest.fixture
def  user_data(request):
    request.cls.login = faker.user_name()
    request.cls.password = faker.password()

@pytest.fixture(name="DR")
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver

@pytest.fixture #(autouse=True)
def driver_use(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    print("Before")
    yield
    print("After")
    driver.quit()

@pytest.fixture(autouse=True)
def setup_environment():

    properties = {

    "STAGE" : os.environ["STAGE"],
    "BROWSER": os.environ["BROWSER"],
    "PYTHON" : os.environ["PYTHON"],
    "MR": os.environ["MR"]
 }
    with open ("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")
