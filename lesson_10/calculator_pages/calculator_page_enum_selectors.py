from enum import Enum

from selenium.webdriver.common.by import By


class CalculatorSelector(Enum):
    """
    Класс для работы с CSS селекторами на странице Калькулятора
    """

    ANY_BUTTON = (By.CSS_SELECTOR, "span.btn")
    INPUT_DELAY = (By.ID, 'delay')
    CALCULATOR_FORM = (By.ID, 'calculator')
    RESULT_SCREEN = (By.CSS_SELECTOR, 'div.screen')
