import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils_instance():
    """
    Фикстура, создающая экземпляр класса pytest_cases
    """
    return StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, expected_str', [
    ('hello world', 'Hello world'),
    ('python is awesome', 'Python is awesome'),
    ('zzz...', 'Zzz...'),
    ('Привет', 'Привет'),
    ('привет', 'Привет'),
])
def test_capitalize(string_utils_instance, input_str, expected_str):
    """
    Проверяет, что метод capitalize корректно делает первую букву заглавной для положительных тестов.
    """
    assert string_utils_instance.capitilize(input_str) == expected_str


@pytest.mark.negative_test
@pytest.mark.parametrize('input_str, expected_str', [
    ('1234567890', '1234567890'),
    ('', ''),
    (' ', ' '),
    ('!welcome', '!welcome'),
    ('❌', '❌'),
    ('-!3', '-!3'),
])
def test_capitalize(string_utils_instance, input_str, expected_str):
    """
    Проверяет, что метод capitalize не меняет исходную строку для негативных тестов.
    """
    assert string_utils_instance.capitilize(input_str) == expected_str
