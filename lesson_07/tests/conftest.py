import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
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

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

    logger.info('Chrome WebDriver closed')


@pytest.fixture
def mock_input_data():
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
