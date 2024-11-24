from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу
url = 'http://uitestingplayground.com/dynamicid'
driver.get(url)

# Найти кнопку
button = driver.find_element(By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]")

# Кликнуть по кнопке
button.click()
print("Кнопка нажата")

# Закрытие браузера
driver.quit()
