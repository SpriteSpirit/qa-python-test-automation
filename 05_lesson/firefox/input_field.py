from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Настройка драйвера для Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


# Шаг 1: Открыть страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Найти поле ввода
input_field = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div/input'))
)

#  Шаг 2: Ввести текст в поле ввода 1000
input_field.send_keys("1000")
print(1_000)

#  Шаг 3: Очистить поле
input_field.clear()
print("clear()")

#  Шаг 4: Ввести текст в поле ввода 999
input_field.send_keys("999")
print(999)

# Шаг 5: Закрыть браузер
driver.quit()
