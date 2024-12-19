import pytest
from utilities.logger_utils import logger
from selenium import webdriver


@pytest.fixture(scope="function")
def chrome_driver():
    """
    Фикстура для инициализации Chrome WebDriver.

    Выполняет:
    Создание драйвера с заданными опциями

    Returns:
        WebDriver: инициализированный драйвер Chrome

    Note:
        Использует yield для передачи драйвера в тесты.
        После выполнения всех тестов закрывает браузер через driver.quit()
    """

    driver = webdriver.Chrome()
    yield driver
    driver.quit()

    logger.info('Chrome WebDriver закрыт')


@pytest.fixture(scope="function")
def mock_input_form_data() -> dict:
    """
    Фикстура для создания мока тестовых данных.

    Возвращает:
        dict: Словарь с тестовыми данными.
    """

    return {
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


@pytest.fixture(scope="function")
def mock_login_data() -> dict:
    """
    Фикстура для создания мока тестовых данных для авторизации.

    Возвращает:
        dict: Словарь с тестовыми данными.
    """

    return {
        "login": "standard_user",
        "password": "secret_sauce",
    }


@pytest.fixture(scope="function")
def mock_items_data() -> list:
    """
    Фикстура для создания мока тестовых данных для списка товаров.

    Возвращает:
        list: Список с тестовыми данными.
    """

    return ["sauce labs backpack", "sauce labs bolt t-shirt", "sauce labs onesie"]


@pytest.fixture(scope="function")
def mock_input_order_data() -> dict:
    """
    Фикстура для создания мока тестовых данных пользователя для оформления заказа.

    Возвращает:
        dict: Словарь с тестовыми данными.
    """

    return {
        "first-name": "Иван",
        "last-name": "Петров",
        "postal-code": "190003",
    }
