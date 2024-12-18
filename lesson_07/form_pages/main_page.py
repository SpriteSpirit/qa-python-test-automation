from typing import Tuple

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from lesson_07.form_pages.form_page_enum_selectors import FormSelector


class FormPage:
    """
    Page Object для страницы формы.
    """

    def __init__(self, driver):
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        self.driver = driver

    def open(self):
        """
        Открыть страницу формы.
        """

        self.driver.get(self.url)

    def wait_for_form_to_load(self,  locator: Tuple[str, str], timeout=10):
        """
        Ожидание загрузки формы.
        """

        WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def fill_input_fields(self, input_data: dict) -> None:
        """
        Заполнить поля формы данными из словаря.
        """
        all_form_labels = self.driver.find_elements(*FormSelector.FORM_LABEL.value)

        for label in all_form_labels:
            field_name = label.text.strip()
            if field_name in input_data:
                input_field = label.find_element(*FormSelector.INPUT_FIELD.value)
                input_field.clear()
                input_field.send_keys(input_data[field_name])

    def submit_form(self) -> None:
        """
        Отправить форму.
        """

        submit_button = self.driver.find_element(*FormSelector.SUBMIT_BUTTON.value)
        submit_button.click()

    def get_results(self) -> dict:
        """
        Получить результаты заполнения полей формы.
        """

        results = {}
        all_form_labels_after_click = self.driver.find_elements(*FormSelector.FORM_LABEL.value)

        for label in all_form_labels_after_click:
            div_alert = label.find_element(*FormSelector.DIV_ALERT.value)
            field_name = label.text
            alert_class = div_alert.get_attribute('class')
            results[field_name] = alert_class

        return results
