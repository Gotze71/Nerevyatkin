#Авторизация через куки
import time
import json
import os.path

from selenium import webdriver

from Lesson_16 import cookie
from Lesson_16_1 import CookieManger

LOGIN = ("xpath", "//input[@id='login_email']")
PASSWORD = ("xpath", "//input[@id='password']")
BUTTON = ("xpath", "//button[@id='loginformsubmit']")

driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/ru/login")

cookie_auth = CookieManger(driver)
if os.path.exists("cookie.json"):
    cookie_auth.load()
else:
    driver.find_element(*LOGIN).send_keys('Aleksei')
    driver.find_element(*PASSWORD).send_keys('12345')
    driver.find_element(*BUTTON).click()
    cookie_auth.save()
time.sleep(3)
