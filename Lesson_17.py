#Чекбокс
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")

CHECKBOX = ("xpath", "//label[@for='tree-node-home']")
driver.find_element(*CHECKBOX).click()

time.sleep(3)

#Радиобаттоны
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/radio-button")

YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']")
YES_RADIO_LABEL = ("xpath", "//label[@for='yesRadio']")
driver.find_element(*YES_RADIO_LABEL).click()
print(driver.find_element(*YES_RADIO_BUTTON).is_enabled())
print(driver.find_element(*YES_RADIO_LABEL).is_selected())
#assert driver.find_element(*YES_RADIO_LABEL).is_selected(), "Error in YES_RADIO_LABEL"
time.sleep(3)

IMPRESSIVE_RADIO_BUTTON = ("xpath", "//label[@for='impressiveRadio']")
driver.find_element(*IMPRESSIVE_RADIO_BUTTON).click()
time.sleep(3)

NO_RADIO_BUTTON = ("xpath", "//label[@id='noRadio']")
driver.find_element(*NO_RADIO_BUTTON).click()
print(driver.find_element(*NO_RADIO_BUTTON).is_enabled())
assert driver.find_element(*NO_RADIO_BUTTON).is_enabled(), "Error in NO_RADIO_BUTTON"

time.sleep(3)
#Дропдауны
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/dropdown")

DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")
DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
DROPDOWN.select_by_value('1')

time.sleep(3)

#Мультиселект
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")

MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")

select = driver.find_element(*MULTISELECT)
select.send_keys("Green")
select.send_keys(Keys.ENTER)
select.send_keys("Blue")
select.send_keys(Keys.ENTER)
select.send_keys("Red")
select.send_keys(Keys.ENTER)
select.send_keys("Black")
select.send_keys(Keys.ENTER)

time.sleep(3)