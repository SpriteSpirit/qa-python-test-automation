from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу
url = 'http://uitestingplayground.com/classattr'
driver.get(url)

# Найти кнопку
button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

# Кликнуть по кнопке
button.click()
print("Кнопка нажата")

# Закрытие браузера
driver.quit()
