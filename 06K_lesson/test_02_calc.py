from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator_operations(driver):
    """
    Тестирует вычисления на калькуляторе с различными выражениями.
    """

    def click_button(key):
        xpath = f"//span[text()='{key}' and contains(@class, 'btn')]"
        button = driver.find_element(By.XPATH, xpath)
        button.click()

    # Установка задержки выполнения операций калькулятора на 45 секунд
    delay_input_field = driver.find_element(By.ID, 'delay')
    delay_input_field.clear()
    delay_input_field.send_keys('45')

    # Выполнение операции: 7 + 8 =
    click_button('7')
    click_button('+')
    click_button('8')
    click_button('=')

    # Ожидание результата '15' в поле вывода с максимальным ожиданием 50 секунд
    result_element = WebDriverWait(driver, 50).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div.screen')))
    assert result_element.text == '15', f"Ожидаемый результат '15', но получен '{result_element.text}'"
