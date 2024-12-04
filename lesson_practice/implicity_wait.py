from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# НЕЯВНОЕ ОЖИДАНИЕ
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/ajax")
ajax_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
ajax_button.click()

content = driver.find_element(By.CSS_SELECTOR, '#content')

p_text = content.find_element(By.CSS_SELECTOR, 'p.bg-success').text
print(f'Текст: {p_text}')

sleep(3)
driver.quit()
