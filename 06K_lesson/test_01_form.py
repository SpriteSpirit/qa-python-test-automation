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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    yield driver
    driver.quit()


def test_form_submission_with_valid_data(driver):
    """
    Тестирует заполнение полей формы.
    """

    input_data = {
        "First name": "Иван",
        "Last name": "Петров",
        "Address": "Ленина, 55-3",
        "E-mail": "test@skypro.com",
        "Phone number": "+7985899998787",
        "Zip code": "",
        "City": "Москва",
        "Country": "Россия",
        "Job position": "QA",
        "Company": "SkyPro"
    }

    form_label_selector = '.form-label'
    submit_button_selector = 'button[type=submit]'
    input_field_selector = 'input'
    div_alert_selector = 'div'

    WebDriverWait(driver, 10, 0.1).until(
        ec.presence_of_element_located(
            (By.CSS_SELECTOR, form_label_selector),
        )
    )

    all_form_labels = driver.find_elements(By.CSS_SELECTOR, form_label_selector)
    submit_button = driver.find_element(By.CSS_SELECTOR, submit_button_selector)

    for label in all_form_labels:
        for field_name, field_value in input_data.items():
            if label.text == field_name:
                input_field = label.find_element(By.CSS_SELECTOR, input_field_selector)
                input_field.clear()
                input_field.send_keys(field_value)

    submit_button.click()

    all_form_labels_after_click = driver.find_elements(By.CSS_SELECTOR, form_label_selector)

    for label in all_form_labels_after_click:
        div_alert = label.find_element(By.CSS_SELECTOR, div_alert_selector).get_attribute('class')
        field_name = label.text

        if "N/A" not in field_name and "Zip code" not in field_name:
            assert 'success' in div_alert, f"Поле '{field_name}' не выделено зеленым цветом"
        elif "N/A" in field_name and "Zip code" in field_name:
            assert 'danger' in div_alert, f"Zip code поле '{field_name}' не выделено красным"
