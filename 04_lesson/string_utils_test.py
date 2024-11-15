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
def test_capitalize_positive(string_utils_instance, input_str, expected_str):
    """
    Проверяет, что метод capitalize корректно делает первую букву заглавной для позитивных тестов.
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
def test_capitalize_negative(string_utils_instance, input_str, expected_str):
    """
    Проверяет, что метод capitalize не меняет исходную строку для негативных тестов.
    """
    assert string_utils_instance.capitilize(input_str) == expected_str


@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, expected_str', [
    ('    hello world', 'hello world'),                 # Проверка удаления пробелов в начале
    (' python is awesome ', 'python is awesome '),      # Пробелы в начале удаляются, пробелы в конце остаются
    ('     ', ''),                                      # Проверка удаления всех пробелов в начале
    (' . . ', '. . '),                                  # Проверка сохранения пробелов внутри строки
    ('Sun', 'Sun'),                                     # Проверка строки без пробелов
    (' a', 'a'),                                        # Проверка удаления пробела в начале
    ('abc   ', 'abc   '),                               # Пробелы в конце остаются
    ('\t hello', '\t hello'),                           # Проверка, что табуляция не удаляется
    ('\n hello', '\n hello'),                           # Проверка, что перенос строки не удаляется
    (' \n hello', '\n hello'),                          # Комбинация пробела и специальных символов
    (' ' * 1000 + 'text', 'text'),                      # Очень много пробелов в начале
    ('  \t\n hello', '\t\n hello'),                     # Комбинация разных пробельных символов
    (' \r\n text', '\r\n text'),                        # Возврат каретки
    ('   \v text', '\v text'),                          # Вертикальная табуляция
    (' ' + 'x' * 1000, 'x' * 1000),                     # Длинная строка после пробела
    ('\t \n \r hello', '\t \n \r hello'),               # Комбинация различных whitespace символов
    ('\r hello', '\r hello'),                           # Проверка, что возврат каретки не удаляется
])
def test_trim_positive(string_utils_instance, input_str, expected_str):
    """
    Проверяет, что метод trim корректно удаляет пробелы в начале строки для позитивных тестов.
    """
    assert string_utils_instance.trim(input_str) == expected_str


@pytest.mark.negative_test
@pytest.mark.parametrize('input_str, expected_str', [
    ('1234567890', '1234567890'),                       # Числовая строка без пробелов
    ('', ''),                                           # Пустая строка
    ('!123', '!123'),                                   # Строка без пробелов в начале
    ('.   !123', '.   !123'),                           # Строка без пробелов в начале
    ('❌', '❌'),                                       # Строка без пробелов в начале
    ('\u2000text', '\u2000text'),                       # Unicode пробел
    ('\xa0text', '\xa0text'),                           # Non-breaking space
    ('\u3000text', '\u3000text'),                       # Идеографический пробел
    ('　text', '　text'),                                # Полноширинный пробел
    ('\rtext', '\rtext'),                               # Возврат каретки
    ('\vtext', '\vtext'),                               # Вертикальная табуляция
])
def test_trim_negative(string_utils_instance, input_str, expected_str):
    """
    Проверяет, что метод trim не меняет исходную строку для негативных тестов.
    """
    assert string_utils_instance.trim(input_str) == expected_str


@pytest.mark.negative_test
@pytest.mark.parametrize('input_str', [
    None,
    123,
    True,
    ['string'],
    {'key': 'value'}
])
def test_trim_invalid_types(string_utils_instance, input_str):
    """
    Проверяет, что метод trim корректно обрабатывает неверные типы данных
    """
    with pytest.raises(AttributeError):
        string_utils_instance.trim(input_str)


@pytest.mark.positive_test
def test_trim_immutability(string_utils_instance):
    """
    Проверяет, что исходная строка не изменяется
    """
    input_str = "  hello"
    original = input_str
    string_utils_instance.trim(input_str)
    assert input_str == original
