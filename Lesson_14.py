import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")
wait = WebDriverWait(driver, 7, poll_frequency = 1)

BUTTON_CLICK_AFTER_5SECONDS = ("xpath", "//button[@id='enableAfter']")

wait.until(EC.element_to_be_clickable(BUTTON_CLICK_AFTER_5SECONDS))

driver.find_element(*BUTTON_CLICK_AFTER_5SECONDS).click()
time.sleep(5)

BUTTON = ("xpath", "//button[@id='visibleAfter']")

wait.until(EC.presence_of_all_elements_located(BUTTON))

driver.find_element(*BUTTON).click()
time.sleep(5)

BUTTON_COLOR_CHANGE = ("xpath", "//button[@id='colorChange']")

wait.until(EC.element_to_be_clickable(BUTTON_COLOR_CHANGE))
driver.find_element(*BUTTON_COLOR_CHANGE).click()
time.sleep(5)





