import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

#Full Name
full_name = driver.find_element( "xpath", "//input[@placeholder= 'Full Name'] ")
full_name.clear()
assert full_name.get_attribute("value") == "", "403 Error in full_name"
full_name.send_keys("Aleksei")
full_name.get_attribute("value")
assert full_name.get_attribute("value") == "Aleksei" , "404 Error in full_name"

#Email
email = driver.find_element("xpath", "//input[@type = 'email']")
email.clear()
assert email.get_attribute("value") == "", "403 Error in email"
email.send_keys("barabashka@mail.ru")
email.get_attribute("value")
assert email.get_attribute("value") == "barabashka@mail.ru", "404 Error in email"

#Current Address
current_address = driver.find_element("xpath", "//textarea[@id='currentAddress']")
current_address.clear()
assert current_address.get_attribute("value") == "", "403 Error in current_address"
current_address.send_keys("Moscow")
current_address.get_attribute("value")
assert current_address.get_attribute("value") == "Moscow", "404 Error in current_address"

#Permanent Address
permanent_address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
permanent_address.clear()
assert permanent_address.get_attribute("value") == "", "403 Error in permanent_address"
permanent_address.send_keys("Lyubertsy")
permanent_address.get_attribute("value")
assert permanent_address.get_attribute("value") == "Lyubertsy", "404 Error in permanent_address"

time.sleep(5)

#Ввод данных с клавиатуры
import time
from selenium import webdriver
from selenium.webdriver import Keys
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/key_presses")


INPUT_FIELD = driver.find_element ("xpath", "//input[@id='target']").send_keys("Hello World")
INPUT_FIELD = driver.find_element("xpath", "//input[@id='target']").send_keys(Keys.CONTROL + "A")
time.sleep(5)
INPUT_FIELD = driver.find_element("xpath", "//input[@id='target']").send_keys(Keys.BACKSPACE)
time.sleep(5)