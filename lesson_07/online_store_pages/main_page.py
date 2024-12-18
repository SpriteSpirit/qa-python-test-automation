from typing import Tuple

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class StorePage:
    """
    Page Object для страницы Интернет-магазина.
    """

    def __init__(self, driver):
        self.base_url = "https://www.saucedemo.com/"
        self.driver = driver

    def open(self, relative_url=""):
        """
        Открыть страницу
        """

        self.driver.get(f"{self.base_url}{relative_url}")

    def wait_text_to_be_present_in_element(self, locator: Tuple[str, str], text: str, timeout=10):
        """
        Ожидание загрузки результата и проверки содержания текста
        """

        WebDriverWait(self.driver, timeout).until(ec.text_to_be_present_in_element(locator, text))

    def wait_presence_of_element(self, locator: Tuple[str, str], timeout=10):
        """
        Ожидание загрузки элемента и возвращает элемент
        """

        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def wait_presence_of_elements(self, locator: Tuple[str, str], timeout=10):
        """
        Ожидание загрузки элементов и возвращает элементы
        """

        return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))
