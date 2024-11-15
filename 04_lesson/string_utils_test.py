import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils_instance():
    """
    Фикстура, создающая экземпляр класса pytest_cases
    """
    return StringUtils()


# ------------- test_capitalize ------------- #
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


# ------------- test_trim ------------- #
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


# ------------- test_to_list ------------- #
@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, input_delimiter, expected_str', [
    # Тесты на граничные случаи
    (',,,', ',', ['', '', '', '']),                 # Только разделители
    ('a,,b,,c', ',', ['a', '', 'b', '', 'c']),      # Пустые значения между разделителями
    ('abc', ',', ['abc']),                          # Строка без разделителей
    (',', ',', ['', '']),                           # Один разделитель
    ('a,b,c,', ',', ['a', 'b', 'c', '']),           # Разделитель в конце
    (',a,b,c', ',', ['', 'a', 'b', 'c']),           # Разделитель в начале
    # Тесты на специальные символы
    ('a\nb\nc', '\n', ['a', 'b', 'c']),             # Перенос строки как разделитель
    ('a\tb\tc', '\t', ['a', 'b', 'c']),             # Табуляция как разделитель
    ('a|b|c', '|', ['a', 'b', 'c']),                # Спецсимвол как разделитель
    ('a.b.c', '.', ['a', 'b', 'c']),                # Точка как разделитель
    # Тесты на многосимвольные разделители
    ('a:::b:::c', ':::', ['a', 'b', 'c']),          # Длинный разделитель
    ('a<->b<->c', '<->', ['a', 'b', 'c']),          # Составной разделитель
    ('aANDbANDc', 'AND', ['a', 'b', 'c']),          # Словесный разделитель
    # Тесты на Unicode
    ('α,β,γ', ',', ['α', 'β', 'γ']),                # Греческие буквы
    ('😀,😂,😎', ',', ['😀', '😂', '😎']),         # Эмодзи
    ('привет,мир', ',', ['привет', 'мир']),         # Кириллица
])
def test_to_list_with_delimiter_positive(string_utils_instance, input_str, input_delimiter, expected_str):
    """
    Проверяет, что метод с разделителем возвращает ожидаемый результат при позитивных проверках.
    """
    assert StringUtils.to_list(string_utils_instance, input_str, input_delimiter) == expected_str


@pytest.mark.positive_test
def test_to_list_immutability_default(string_utils_instance):
    """
    Проверяет, что исходная строка не изменяется. Разделитель по умолчанию.
    """
    input_str = "a,b,c"
    original = input_str
    string_utils_instance.to_list(input_str)
    assert input_str == original


@pytest.mark.negative_test
@pytest.mark.parametrize('input_str, input_delimiter, expected_str', [
    ('1234567890', '123', ['', '4567890']),
    ('', ',', []),  # Пустая строка
    ('   ', ',', []),  # Строка с пробелами
    ('a,b,c', '', ValueError),  # Пустой разделитель
])
def test_to_list_with_delimiter_negative(string_utils_instance, input_str, input_delimiter, expected_str):
    """
    Проверяет, что метод возвращает ожидаемый результат при негативных проверках с использованием разделителя.
    """
    if expected_str is ValueError:
        with pytest.raises(ValueError):
            string_utils_instance.to_list(input_str, input_delimiter)
    else:
        assert string_utils_instance.to_list(input_str, input_delimiter) == expected_str


@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, expected_str', [
    ('Everyday - I try and I try and I try', ['Everyday - I try and I try and I try']),
    ('I work, till, I ache, in my bones', ['I work', ' till', ' I ache', ' in my bones']),
    ('Ooh-each-morning-I-get-up-I-die-a-little', ['Ooh-each-morning-I-get-up-I-die-a-little']),
    ('Ah, got no common sense', ['Ah', ' got no common sense']),
])
def test_to_list_default(string_utils_instance, input_str, expected_str):
    """
    Проверяет, что метод возвращает ожидаемый результат при использовании разделителя по умолчанию.
    """
    assert StringUtils.to_list(string_utils_instance, input_str) == expected_str


@pytest.mark.positive_test
def test_to_list_long_string(string_utils_instance):
    """
    Проверяет работу метода с длинной строкой.
    """
    long_str = ','.join(['a'] * 1000)  # Строка с 1000 элементами
    result = string_utils_instance.to_list(long_str, ',')
    assert len(result) == 1000
    assert all(x == 'a' for x in result)


@pytest.mark.negative_test
@pytest.mark.parametrize('input_str, input_delimiter', [
    (None, ','),          # None как входная строка
    (123, ','),           # Число как входная строка
    (True, ','),          # Boolean как входная строка
    (['a', 'b'], ','),    # Список как входная строка
    ({'a': 1}, ','),      # Словарь как входная строка
])
def test_to_list_invalid_input_types(string_utils_instance, input_str, input_delimiter):
    """
    Проверяет обработку некорректных типов входной строки
    """
    with pytest.raises((AttributeError, TypeError)):
        string_utils_instance.to_list(input_str, input_delimiter)


@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, input_delimiter, expected_str', [
    ('a b c', None, ['a', 'b', 'c']),          # None как разделитель (разделение по пробелам)
    ('a   b   c', None, ['a', 'b', 'c']),      # Множественные пробелы
    ('a\tb\nc', None, ['a', 'b', 'c']),        # Разные типы пробельных символов
])
def test_to_list_none_delimiter(string_utils_instance, input_str, input_delimiter, expected_str):
    """
    Проверяет, что при передаче None в качестве разделителя метод разделяет строку по пробелам
    """
    assert string_utils_instance.to_list(input_str, input_delimiter) == expected_str
