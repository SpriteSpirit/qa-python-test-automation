from typing import Tuple

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from lesson_07.calculator_pages.calculator_page_enum_selectors import CalculatorSelector
# from utilities.logger_utils import logger


class CalculatorPage:
    """
    Page Object для страницы Медленный калькулятор.
    """

    def __init__(self, driver):
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.driver = driver

    def open(self):
        """
        Открыть страницу
        """

        self.driver.get(self.url)

    def wait_to_load_result_and_compare_text(self, locator: Tuple[str, str], text: str, timeout=10):
        """
        Ожидание загрузки результата и проверки содержания текста
        """

        WebDriverWait(self.driver, timeout).until(ec.text_to_be_present_in_element(locator, text))

    def click_button(self, key: str) -> bool:
        """
        Клик на кнопку калькулятора
        """

        all_buttons = self.driver.find_elements(*CalculatorSelector.ANY_BUTTON.value)
        # logger.debug(f"All buttons: {len(all_buttons)}")

        for button in all_buttons:
            # logger.debug(f"Button: {button.text}")

            if button.text == key:
                button.click()

                return True
        else:
            return False

    def set_delay(self, delay_time: int) -> None:
        """
        Устанавливает задержку выполнения операций калькулятора на delay_time секунд
        """

        delay_input_field = self.driver.find_element(*CalculatorSelector.INPUT_DELAY.value)

        delay_input_field.clear()
        delay_input_field.send_keys(delay_time)
