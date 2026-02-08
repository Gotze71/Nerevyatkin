#1
import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 OPR/124.0.0.0')

driver = webdriver.Chrome(options=options)
driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
time.sleep(5)

#2
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 CriOS/138.0.7204.524 YaBrowser/25.8.3.524.10 SA/3 Mobile/15E148 Safari/604.1')
options.add_argument("--disable-blink-features=AutomationExtension")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--remote-debugging-port=9222")
driver_call = webdriver.Chrome(options=options)
driver_call.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')

time.sleep(5)

#3
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 7, poll_frequency=0.5)
driver.get('https://demoqa.com/alerts')

FIRST_BUTTON = ("xpath", "//button[@id='alertButton']")
driver.find_element(*FIRST_BUTTON).click()

alert = wait.until(EC.alert_is_present())
alert.accept()

time.sleep(5)

#4
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 7, poll_frequency=0.5)
driver.get('https://demoqa.com/alerts')

THIRD_BUTTON = ("xpath", "//button[@id='confirmButton']")
driver.find_element(*THIRD_BUTTON).click()

alert = wait.until(EC.alert_is_present())
alert.accept()
time.sleep(5)

driver.find_element(*THIRD_BUTTON).click()

alert = wait.until(EC.alert_is_present())
alert.dismiss()
time.sleep(5)

#5
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, poll_frequency=0.5)
driver.get('https://demoqa.com/alerts')

FOURTH_BUTTON = ("xpath", "//button[@id='promtButton']")
driver.find_element(*FOURTH_BUTTON).click()

alert = wait.until(EC.alert_is_present())
alert.send_keys('Aleksei')

time.sleep(5)

alert.accept()

time.sleep(5)

#6
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_12 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/395.0.830179879 Mobile/15E148 Safari/604.1')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"] )
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=0.5)
driver.get('https://demoqa.com/alerts')

BUTTON = ("xpath", "//button[@id='promtButton']")
driver.find_element(*BUTTON).click()

alert = wait.until(EC.alert_is_present())
alert.send_keys('Aleksei')

time.sleep(5)

alert.accept()

time.sleep(5)
