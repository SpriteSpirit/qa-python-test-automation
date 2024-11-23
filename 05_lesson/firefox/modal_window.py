from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера для Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    # Шаг 1: Открыть страницу
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # Шаг 2: Явное ожидание появления модального окна
    modal_close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p'))
    )

    # Ожидание 3 сек.
    sleep(3)

    # Шаг 3: Нажать на кнопку "Close" в модальном окне
    modal_close_button.click()
    print("Модальное окно закрыто.")

    # Ожидание 3 сек.
    sleep(3)
finally:
    # Шаг 4: Закрыть браузер
    driver.quit()