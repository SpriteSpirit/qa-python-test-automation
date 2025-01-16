import allure
from utilities.logger_utils import logger
from lesson_07.form_pages.main_page import FormPage
from lesson_07.form_pages.form_page_enum_selectors import FormSelector


@allure.title("Тестирование заполнения и отправки формы")
@allure.label("owner", "khalueva.angelina")
@allure.feature("Страница отправки формы")
@allure.description("Проверяет заполнение и отправку формы.")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_page(chrome_driver, mock_input_form_data):
    """
    Тестирование заполнения и отправки формы.
    """

    with allure.step("Создание экземпляра FormPage"):
        logger.debug("Создание экземпляра FormPage")
        form_page = FormPage(chrome_driver)

    with allure.step("Открытие страницы формы"):
        logger.debug("Открытие страницы формы")
        form_page.open()

    with allure.step("Ожидание загрузки формы"):
        logger.debug("Ожидание загрузки формы")
        form_page.wait_for_form_to_load(FormSelector.FORM_LABEL.value)

    with allure.step("Заполнение полей формы"):
        logger.debug("Заполнение полей формы")
        form_page.fill_input_fields(mock_input_form_data)

    with allure.step("Отправка формы"):
        logger.debug("Отправка формы")
        form_page.submit_form()

    with allure.step("Получение и проверка результатов"):
        logger.debug("Получение результатов")
        results = form_page.get_results()

        logger.debug("Проверка результатов")

        for field_name, div_class in results.items():
            if 'N/A' not in field_name and 'Zip code' not in field_name:
                assert 'success' in div_class, \
                    f"Поле '{field_name}' не прошло проверку: ожидается класс 'success'"
            elif 'Zip code' in field_name:
                assert 'danger' in div_class, \
                    f"Поле '{field_name}' не прошло проверку: ожидается класс 'danger' для Zip code"
            elif 'N/A' in field_name:
                assert 'danger' in div_class, \
                    f"Поле '{field_name}' не прошло проверку: ожидается класс 'danger' для N/A"
