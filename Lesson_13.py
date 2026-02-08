#Опции
import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/text-box")

INPUT_FIELD = ("xpath", "//input[@placeholder= 'Full Name']")
full_name = driver.find_element(*INPUT_FIELD)
full_name.clear()
full_name.get_attribute("value")
assert full_name.get_attribute("value") == "", "403 Error"
full_name.send_keys("Alex")
full_name.get_attribute("value")
assert full_name.get_attribute("value") == "Alex", "404 Error"
time.sleep(10)

#Загрузка файлов
import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/upload-download")
LOADING_BUTTON = ("xpath", "//input[@type = 'file']")
button_load = driver.find_element(*LOADING_BUTTON)
button_load.send_keys(r"C:\Users\marat\PycharmProjects\Nerevyatkin\knopka.png")
time.sleep(10)

import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-cache")
driver=webdriver.Chrome(options=options)
driver.get("https://ru.files.me")
LOAD_BUTTON = ("xpath", "//input[@id = 'file_upload']")
button_loading = driver.find_element(*LOAD_BUTTON)
button_loading.send_keys(r"C:\Users\marat\PycharmProjects\Nerevyatkin\knopka.png")
time.sleep(10)