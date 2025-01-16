from enum import Enum

from selenium.webdriver.common.by import By


class FormSelector(Enum):
    """
    Класс для работы с CSS селекторами на странице формы
    """

    FORM_LABEL = (By.CSS_SELECTOR, 'label.form-label')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type=submit]')
    INPUT_FIELD = (By.CSS_SELECTOR, 'input.form-control')
    DIV_ALERT = (By.CSS_SELECTOR, '.alert')
