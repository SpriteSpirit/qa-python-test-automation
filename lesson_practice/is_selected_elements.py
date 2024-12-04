from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://the-internet.herokuapp.com/checkboxes")
checkbox = driver.find_element(By.CSS_SELECTOR, "input[type=checkbox]")
checkbox.is_selected()
print(checkbox.is_selected())
sleep(3)
checkbox.click()
checkbox = driver.find_element(By.CSS_SELECTOR, "input[type=checkbox]")
checkbox.is_selected()
print(checkbox.is_selected())

sleep(5)
driver.quit()
