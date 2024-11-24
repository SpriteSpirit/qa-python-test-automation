from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Настройка драйвера для Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Шаг 1: Открыть страницу
driver.get("http://the-internet.herokuapp.com/login")

# Найти поле username
username_field = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.ID, "username"))
)

# Шаг 2: Ввести имя пользователя
username_field.send_keys("tomsmith")

# Найти поле password
password_field = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.ID, "password"))
)

# Шаг 3: Ввести пароль
password_field.send_keys("SuperSecretPassword!")

# Найти кнопку "Login"
login_button = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH, '//*[@id="login"]/button'))
)

# Шаг 4: Нажать на кнопку "Login"
login_button.click()

# Шаг 5: Закрыть браузер
driver.quit()
