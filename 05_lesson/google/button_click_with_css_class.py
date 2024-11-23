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
button = driver.find_element(By.CSS_SELECTOR, "button.class2")

# Кликнуть по кнопке
button.click()
print("Кнопка нажата")

# Ожидание 5 сек
sleep(5)

# Закрытие браузера
driver.quit()
