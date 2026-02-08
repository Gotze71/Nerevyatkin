#Нажатие кнопок мыши
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, poll_frequency= 0.5)
action = ActionChains(driver)

driver.get("https://demoqa.com/buttons")

DOUBLE_CLICK_BUTTON = ('xpath', '//button[@id="doubleClickBtn"]')
RIGHT_CLICK_BUTTON = ('xpath', '//button[@id="rightClickBtn"]')
CLICK_BUTTON = ('xpath', '//button[text()="Click Me"]')

DOUBLE_CLICK = driver.find_element(*DOUBLE_CLICK_BUTTON)
RIGHT_CLICK = driver.find_element(*RIGHT_CLICK_BUTTON)
CLICK = driver.find_element(*CLICK_BUTTON)

action.double_click(DOUBLE_CLICK).pause(2).context_click(RIGHT_CLICK).pause(2).click(CLICK).pause(2).perform()

time.sleep(3)

#Наведение курсора на обьект
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

options= Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 7, poll_frequency= 1)
action = ActionChains(driver)

driver.get("https://demoqa.com/menu")

BUTTON_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
BUTTON_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
BUTTON_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")

BUTTON_1 = driver.find_element(*BUTTON_1_LOCATOR)
BUTTON_2 = driver.find_element(*BUTTON_2_LOCATOR)
BUTTON_3 = driver.find_element(*BUTTON_3_LOCATOR)

action.move_to_element(BUTTON_1).pause(3).move_to_element(BUTTON_2).pause(3).move_to_element(BUTTON_3).pause(3).perform()

time.sleep(3)

#Перемещение объекта
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency= 1)
action = ActionChains(driver)

driver.get("https://demoqa.com/droppable")

SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")
TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")

SOURCE = driver.find_element(*SOURCE_LOCATOR)
TARGET = driver.find_element(*TARGET_LOCATOR)

action.drag_and_drop(SOURCE, TARGET).perform()

time.sleep(3)