import allure
from utilities.logger_utils import logger
from lesson_07.calculator_pages.main_page import CalculatorPage
from lesson_07.calculator_pages.calculator_page_enum_selectors import CalculatorSelector


@allure.title("Calculator page test")
@allure.tag("web")
@allure.label("owner", "khalueva.angelina")
@allure.story("Calculator page")
@allure.description("Этот тест проверяет результат сложения двух операндов на калькуляторе через 45 с.")
@allure.severity(allure.severity_level.NORMAL)
def test_form_page(chrome_driver):
    """
    Тестирование заполнения и отправки формы.
    """

    delay_time = 45
    timeout = delay_time + 5
    expected_result = 15
    operation_list = ['7', '+', '8', '=']

    with allure.step("Создание экземпляра CalculatorPage"):
        logger.debug("Создание экземпляра CalculatorPage")
        calculator_page = CalculatorPage(chrome_driver)

    with allure.step("Открытие страницы калькулятора"):
        logger.debug("Открытие страницы калькулятора")
        calculator_page.open()

    with allure.step("Проверка, что страница калькулятора открылась правильно"):
        current_url = chrome_driver.current_url
        expected_url = calculator_page.url

        assert current_url == expected_url, (f"Открыта неверная страница. Ожидалось: {expected_url}, "
                                             f"фактически: {current_url}")

    with allure.step(f"Установить задержку выполнения операций калькулятора на {delay_time} с."):
        logger.debug(f"Установить задержку выполнения операций калькулятора на {delay_time} с.")

        assert delay_time >= 0, "Ожидание должно быть положительным значением"

        calculator_page.set_delay(delay_time=delay_time)

    with allure.step("Выполнение операции сложения"):
        logger.debug("Выполнение операции сложения")

        assert operation_list, "Список операций пуст"

        for operand in operation_list:
            success = calculator_page.click_button(operand)

            assert success, f"Не удалось нажать кнопку '{operand}'"

    with allure.step(f"Ожидание {delay_time} с. и проверка результата вычислений"):
        logger.debug(f"Ожидание {delay_time} с. и проверка результата вычислений")

        try:
            calculator_page.wait_to_load_result_and_compare_text(CalculatorSelector.RESULT_SCREEN.value,
                                                                 text=str(expected_result), timeout=timeout)
        except Exception as e:
            assert False, f"Не удалось получить результат '{expected_result}'. Ошибка: {str(e)}"
