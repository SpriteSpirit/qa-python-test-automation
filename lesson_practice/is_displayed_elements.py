from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/visibility")

is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
print(is_displayed)
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#hideButton").click()
sleep(2)
is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
print(is_displayed)

sleep(5)
driver.quit()
