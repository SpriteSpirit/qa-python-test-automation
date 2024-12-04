from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# ЯВНОЕ ОЖИДАНИЕ
waiter = WebDriverWait(driver, 40, 0.1)

driver.get("http://uitestingplayground.com/progressbar")

start_btn = driver.find_element(By.CSS_SELECTOR, '#startButton')
start_btn.click()

waiter.until(
    ec.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '#progressBar'),
        "75%"
    )
)

driver.find_element(By.CSS_SELECTOR, '#stopButton').click()

print(driver.find_element(By.CSS_SELECTOR, '#result').text)

sleep(3)
driver.quit()
