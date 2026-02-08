#Сохранение и чтение кук в файле
import json
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/ru/login")

LOGIN = ("xpath", "//input[@id='login_email']")
PASSWORD = ("xpath", "//input[@id='password']")
BUTTON = ("xpath", "//button[@id='loginformsubmit']")

driver.get("https://www.freeconferencecall.com/ru/ru/login")
driver.find_element(*LOGIN).send_keys("alekseiN@yandex.ru")
driver.find_element(*PASSWORD).send_keys("12345")
driver.find_element(*BUTTON).click()

cookies_auth = driver.get_cookies()

with open("cookies.json", "w") as file:
    json.dump(cookies_auth, file, indent=4)

driver.get("https://www.freeconferencecall.com/ru/ru/login")
driver.delete_all_cookies()

with open ("cookies.json", "r") as file:
    cookies = json.load(file)
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()