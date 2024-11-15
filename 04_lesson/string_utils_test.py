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
    ('', ',', []),              # Пустая строка
    ('   ', ',', []),           # Строка с пробелами
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


# ------------- test_contains ------------- #
@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, input_symbol, expected_bool', [
    # Базовые проверки
    ('Hello, World!', 'H', True),   # Символ в начале
    ('Hello, World!', '!', True),   # Символ в конце
    ('Hello, World!', 'o', True),   # Символ в середине
    ('Hello, World!', 'x', False),  # Отсутствующий символ

    # Специальные символы
    ('Hello\nWorld', '\n', True),   # Перенос строки
    ('Hello\tWorld', '\t', True),   # Табуляция
    ('Hello\\World', '\\', True),   # Обратный слэш
    ('text\r', '\r', True),         # Возврат каретки
    ('text\v', '\v', True),         # Вертикальная табуляция
    ('text\f', '\f', True),         # Перевод страницы

    # Unicode символы
    ('Привет', 'и', True),          # Кириллица
    ('Hello, 世界', '世', True),     # Китайские символы
    ('Hello, 🌍', '🌍', True),      # Эмодзи
    ('⌘⌃⌥⇧', '⌘', True),           # Символы Mac
    ('∑∏∐∆', '∑', True),           # Математические символы
    ('αβγδ', 'β', True),           # Греческие буквы

    # Регистр
    ('Hello', 'h', False),          # Регистрозависимый поиск
    ('HELLO', 'h', False),          # Регистрозависимый поиск

    # Пробельные символы
    ('   ', ' ', True),             # Строка из пробелов
    ('\t\n\r', '\t', True),         # Различные пробельные символы

    # Граничные случаи
    ('a', 'a', True),               # Одиночный символ
    ('aa', 'a', True),              # Повторяющийся символ
    ('', 'a', False),               # Пустая строка
    (' ', '', True),                # Пустой символ в непустой строке
    ('\0', '\0', True),             # Нулевой символ
    ('abc\0def', '\0', True),       # Нулевой символ внутри строки
])
def test_contains_positive(string_utils_instance, input_str, input_symbol, expected_bool):
    """
    Расширенное тестирование метода
    """
    assert string_utils_instance.contains(input_str, input_symbol) == expected_bool


@pytest.mark.negative_test
@pytest.mark.parametrize('input_str, input_symbol, expected_result', [
    ('text', 'ab', False),      # Поиск подстроки вместо одного символа
    (['a'], 'a', True),         # Список в качестве строки
])
def test_contains_negative_values(string_utils_instance, input_str, input_symbol, expected_result):
    """
    Проверяет обработку некорректных входных данных, которые должны вернуть False
    """
    assert string_utils_instance.contains(input_str, input_symbol) == expected_result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_str, input_symbol, expected_error', [
    ('text', ['a'], TypeError),                 # Список в качестве символа
    ('text', 123, TypeError),                   # Число в качестве символа
    ('text', None, TypeError),                  # None в качестве символа
    ({'a': 1}, 'a', AttributeError),            # Словарь в качестве строки
    (True, 'a', AttributeError),                # Boolean в качестве строки
    (None, 'a', AttributeError),                # None в качестве строки
    (123, 'a', AttributeError),                 # Число в качестве строки
    ('text', object(), TypeError),              # Объект как символ
    ('text', float(1.0), TypeError),            # Float как символ
    (b'bytes', 'a', TypeError),                 # Bytes как строка
    (bytearray(b'text'), 'a', TypeError),       # Bytearray как строка
])
def test_contains_exceptions(string_utils_instance, input_str, input_symbol, expected_error):
    """
    Проверяет, что метод вызывает исключения при определенных некорректных входных данных
    """
    with pytest.raises(expected_error):
        string_utils_instance.contains(input_str, input_symbol)


@pytest.mark.positive_test
def test_contains_immutability(string_utils_instance):
    """
    Проверяет, что входные данные не изменяются
    """
    input_str = "Hello, World!"
    input_symbol = "o"
    original_str = input_str
    original_symbol = input_symbol

    string_utils_instance.contains(input_str, input_symbol)

    assert input_str == original_str
    assert input_symbol == original_symbol


@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, input_symbol, expected_bool', [
    ('👨‍👩‍👧‍👦', '👨', True),    # Составной эмодзи
    ('🏳️‍🌈', '🏳️', True),    # Эмодзи с модификатором
    ('👨🏻‍💻', '👨', True),    # Эмодзи с тоном кожи
])
def test_contains_complex_unicode(string_utils_instance, input_str, input_symbol, expected_bool):
    """
    Проверяет работу с составными Unicode символами
    """
    assert string_utils_instance.contains(input_str, input_symbol) == expected_bool


@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, input_symbol, expected_bool', [
    (' \t\n\r\f\v', ' ', True),     # Все виды пробельных символов
    ('\u2000', '\u2000', True),     # Unicode пробел
    ('\xa0', '\xa0', True),         # Non-breaking space
])
def test_contains_whitespace(string_utils_instance, input_str, input_symbol, expected_bool):
    """
    Проверяет работу с различными видами пробельных символов
    """
    assert string_utils_instance.contains(input_str, input_symbol) == expected_bool


# ------------- test_delete_symbol ------------- #
@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, input_symbol, expected_str', [
    # Базовые проверки
    ('Hello, World!', 'H', 'ello, World!'),   # Символ в начале
    ('Hello, World!', '!', 'Hello, World'),   # Символ в конце
    ('Hello, World!', 'o', 'Hell, Wrld!'),   # Символ в середине
    ('Hello, World!', 'x', 'Hello, World!'),  # Отсутствующий символ

    # Специальные символы
    ('Hello\nWorld', '\n', 'HelloWorld'),     # Перенос строки
    ('Hello\tWorld', '\t', 'HelloWorld'),     # Табуляция
    ('Hello\\World', '\\', 'HelloWorld'),     # Обратный слэш
    ('text\r', '\r', 'text'),                 # Возврат каретки
    ('text\v', '\v', 'text'),                 # Вертикальная табуляция
    ('text\f', '\f', 'text'),                 # Перевод страницы

    # Unicode символы
    ('Привет', 'и', 'Првет'),                   # Кириллица
    ('Hello, 世界', '世', 'Hello, 界'),           # Китайские символы
    ('Hello, 🌍', '🌍', 'Hello, '),             # Эмодзи
    ('⌘⌃⌥⇧', '⌘', '⌃⌥⇧'),                       # Символы Mac
    ('∑∏∐∆', '∑', '∏∐∆'),                       # Математические символы
    ('αβγδ', 'β', 'αγδ'),                       # Греческие буквы

    # Регистр
    ('Hello', 'h', 'Hello'),                    # Регистрозависимый поиск
    ('HELLO', 'h', 'HELLO'),                    # Регистрозависимый поиск

    # Пробельные символы
    ('   ', ' ', ''),                           # Строка из пробелов
    ('\t\n\r', '\t', '\n\r'),                   # Различные пробельные символы

    # Граничные случаи
    ('a', 'a', ''),                             # Одиночный символ
    ('aa', 'a', ''),                            # Повторяющийся символ
    ('', 'a', ''),                              # Пустая строка
    (' ', '', ' '),                             # Пустой символ в непустой строке
    ('', '', ''),                               # Пустая строка и пустой символ
    ('\0', '\0', ''),                           # Нулевой символ
    ('abc\0def', '\0', 'abcdef'),               # Нулевой символ внутри строки
    ('text', '', 'text'),                       # Пустой символ для поиска

    # Удаление подстрок
    ('SkyPro', 'Pro', 'Sky'),                   # Как в примере из документации
    ('TestTest', 'Test', ''),                   # Повторяющаяся подстрока
    ('abcabc', 'abc', ''),                      # Последовательное удаление
    ('Hello World', 'o W', 'Hellorld'),         # Подстрока с пробелом
    ('TestMiddleTest', 'Middle', 'TestTest'),   # Подстрока в середине
    ('PreTestPost', 'Test', 'PrePost'),         # Подстрока с окружением
    ('Te[st]Te[st]', '[st]', 'TeTe'),           # Подстрока со спецсимволами
    ('Hello  World', '  ', 'HelloWorld'),       # Подстрока из пробелов
    ('abc123abc123', '123', 'abcabc'),          # Подстрока из цифр
    ('Test_Test', '_', 'TestTest'),             # Одиночный символ как разделитель

    # Множественное удаление
    ('aaa', 'a', ''),                           # Удаление всех вхождений
    ('a.b.c.d', '.', 'abcd'),                   # Удаление разделителя
    ('111222333', '2', '111333'),               # Удаление цифр
    ('  a  b  c  ', ' ', 'abc'),                # Удаление пробелов
])
def test_delete_symbol_positive(string_utils_instance, input_str, input_symbol, expected_str):
    """
    Расширенное тестирование метода
    """
    assert string_utils_instance.delete_symbol(input_str, input_symbol) == expected_str


@pytest.mark.negative_test
@pytest.mark.parametrize('input_str, input_symbol, expected_result', [
    ('text', 'ab', 'text'),     # Поиск подстроки вместо одного символа
    ('', 'a', ''),              # Пустая строка
])
def test_delete_symbol_negative_values(string_utils_instance, input_str, input_symbol, expected_result):
    """
    Проверяет обработку некорректных входных данных
    """
    assert string_utils_instance.delete_symbol(input_str, input_symbol) == expected_result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_str, input_symbol, expected_error', [
    ('text', ['a'], TypeError),                 # Список в качестве символа
    ('text', 123, TypeError),                   # Число в качестве символа
    ('text', None, TypeError),                  # None в качестве символа
    ({'a': 1}, 'a', AttributeError),            # Словарь в качестве строки
    (True, 'a', AttributeError),                # Boolean в качестве строки
    (None, 'a', AttributeError),                # None в качестве строки
    (123, 'a', AttributeError),                 # Число в качестве строки
    ('text', object(), TypeError),              # Объект как символ
    ('text', float(1.0), TypeError),            # Float как символ
    (b'bytes', 'a', TypeError),                 # Bytes как строка
    (bytearray(b'text'), 'a', TypeError),       # Bytearray как строка
    (['a'], 'a', AttributeError),               # Список в качестве строки
])
def test_delete_symbol_exceptions(string_utils_instance, input_str, input_symbol, expected_error):
    """
    Проверяет, что метод вызывает исключения при некорректных входных данных
    """
    with pytest.raises(expected_error):
        string_utils_instance.delete_symbol(input_str, input_symbol)


@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, input_symbol, expected_str', [
    # Простые эмодзи
    ('👨👩👧👦', '👨', '👩👧👦'),  # Отдельные эмодзи
    ('🌍🌎test', '🌍', '🌎test'),   # Простой эмодзи в начале
    ('code🎮', '🎮', 'code'),        # Простой эмодзи в конце
    ('👨‍👩‍👧‍👦', '👨', '‍👩‍👧‍👦'),              # Составной эмодзи

    # Одиночные эмодзи с модификаторами
    ('👩🏻👩🏼👩🏽', '👩🏻', '👩🏼👩🏽'),       # Эмодзи с тоном кожи
    ('🚩🏳️🏴', '🏳️', '🚩🏴'),       # Эмодзи с вариационным селектором
])
def test_delete_symbol_complex_unicode(string_utils_instance, input_str, input_symbol, expected_str):
    """
    Проверяет работу с составными Unicode символами
    """
    assert string_utils_instance.delete_symbol(input_str, input_symbol) == expected_str


@pytest.mark.positive_test
def test_delete_symbol_immutability(string_utils_instance):
    """
    Проверяет, что входные данные не изменяются
    """
    input_str = "Hello, World!"
    input_symbol = "o"
    original_str = input_str
    original_symbol = input_symbol

    string_utils_instance.delete_symbol(input_str, input_symbol)

    assert input_str == original_str
    assert input_symbol == original_symbol


# ------------- test_starts_with ------------- #
@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, input_symbol, expected_bool', [
    # Базовые проверки
    ('Hello, World!', 'H', True),    # Символ в начале
    ('Hello, World!', '!', False),   # Символ в конце
    ('Hello, World!', 'o', False),   # Символ в середине
    ('Hello, World!', 'x', False),   # Отсутствующий символ

    # Специальные символы
    ('\nHello World', '\n', True),   # Перенос строки
    ('\tHello World', '\t', True),   # Табуляция
    ('\\Hello World', '\\', True),   # Обратный слэш
    ('\rtext', '\r', True),         # Возврат каретки
    ('\vtext', '\v', True),         # Вертикальная табуляция
    ('\ftext', '\f', True),         # Перевод страницы

    # Unicode символы
    ('Привет', 'П', True),         # Кириллица
    ('世界, hello', '世', True),    # Китайские символы
    ('🌍, hello', '🌍', True),     # Эмодзи
    ('⌘⌃⌥⇧', '⌘', True),           # Символы Mac
    ('∑∏∐∆', '∑', True),           # Математические символы
    ('αβγδ', 'α', True),           # Греческие буквы

    # Регистр
    ('Hello', 'h', False),          # Регистрозависимый поиск
    ('hello', 'H', False),          # Регистрозависимый поиск

    # Пробельные символы
    ('   ', ' ', True),             # Строка из пробелов
    ('\t\n\r', '\t', True),         # Различные пробельные символы

    # Граничные случаи
    ('a', 'a', True),               # Одиночный символ
    ('aa', 'a', True),              # Повторяющийся символ
    ('', 'a', False),               # Пустая строка
    (' ', '', True),                # Пустой символ в непустой строке
    ('\0', '\0', True),             # Нулевой символ
    ('abc\0def', '\0', False),       # Нулевой символ внутри строки
])
def test_starts_with_positive(string_utils_instance, input_str, input_symbol, expected_bool):
    """
    Расширенное тестирование метода
    """
    assert string_utils_instance.starts_with(input_str, input_symbol) == expected_bool


@pytest.mark.negative_test
@pytest.mark.parametrize('input_str, input_symbol, expected_result', [
    ('text', 'ab', False),      # Поиск подстроки вместо одного символа
])
def test_starts_with_negative_values(string_utils_instance, input_str, input_symbol, expected_result):
    """
    Проверяет обработку некорректных входных данных, которые должны вернуть False
    """
    assert string_utils_instance.starts_with(input_str, input_symbol) == expected_result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_str, input_symbol, expected_error', [
    ('text', ['a'], TypeError),                 # Список в качестве символа
    ('text', 123, TypeError),                   # Число в качестве символа
    ('text', None, TypeError),                  # None в качестве символа
    ({'a': 1}, 'a', AttributeError),            # Словарь в качестве строки
    (True, 'a', AttributeError),                # Boolean в качестве строки
    (None, 'a', AttributeError),                # None в качестве строки
    (123, 'a', AttributeError),                 # Число в качестве строки
    ('text', object(), TypeError),              # Объект как символ
    ('text', float(1.0), TypeError),            # Float как символ
    (b'bytes', 'a', TypeError),                 # Bytes как строка
    (bytearray(b'text'), 'a', TypeError),       # Bytearray как строка
    (['a'], 'a', AttributeError),               # Список в качестве строки
])
def test_starts_with_exceptions(string_utils_instance, input_str, input_symbol, expected_error):
    """
    Проверяет, что метод вызывает исключения при определенных некорректных входных данных
    """
    with pytest.raises(expected_error):
        string_utils_instance.starts_with(input_str, input_symbol)


@pytest.mark.positive_test
def test_starts_with_immutability(string_utils_instance):
    """
    Проверяет, что входные данные не изменяются
    """
    input_str = "Hello, World!"
    input_symbol = "o"
    original_str = input_str
    original_symbol = input_symbol

    string_utils_instance.starts_with(input_str, input_symbol)

    assert input_str == original_str
    assert input_symbol == original_symbol


@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, input_symbol, expected_bool', [
    ('👨‍👩‍👧‍👦', '👨', True),    # Составной эмодзи
    ('🏳️‍🌈', '🏳️', True),    # Эмодзи флага с модификатором
    ('👨🏻‍💻', '👨', True),    # Составной эмодзи (человек за компьютером)
])
def test_starts_with_complex_unicode(string_utils_instance, input_str, input_symbol, expected_bool):
    """
    Проверяет работу с составными Unicode символами
    """
    assert string_utils_instance.starts_with(input_str, input_symbol) == expected_bool


@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, input_symbol, expected_bool', [
    (' \t\n\r\f\v', ' ', True),     # Все виды пробельных символов
    ('\u2000', '\u2000', True),     # Unicode пробел
    ('\xa0', '\xa0', True),         # Non-breaking space
])
def test_starts_with_whitespace(string_utils_instance, input_str, input_symbol, expected_bool):
    """
    Проверяет работу с различными видами пробельных символов
    """
    assert string_utils_instance.starts_with(input_str, input_symbol) == expected_bool


# ------------- test_end_with ------------- #
@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, input_symbol, expected_bool', [
    # Базовые проверки
    ('Missing', 'M', False),        # Символ в начале
    ('Hello, World!', '!', True),   # Символ в конце
    ('Hello, World!', 'o', False),  # Символ в середине
    ('Hello, World!', 'x', False),  # Отсутствующий символ

    # Специальные символы
    ('Hello World\n', '\n', True),  # Перенос строки
    ('Hello World\t', '\t', True),  # Табуляция
    ('Hello World\\', '\\', True),  # Обратный слэш
    ('text\r', '\r', True),         # Возврат каретки
    ('text\v', '\v', True),         # Вертикальная табуляция
    ('text\f', '\f', True),         # Перевод страницы

    # Unicode символы
    ('Привет', 'т', True),         # Кириллица
    ('Hello,世界', '界', True),    # Китайские символы
    ('Hello, 🌍', '🌍', True),     # Эмодзи
    ('⌘⌃⌥⇧', '⇧', True),           # Символы Mac
    ('∑∏∐∆', '∆', True),           # Математические символы
    ('αβγδ', 'δ', True),           # Греческие буквы

    # Регистр
    ('Hello', 'O', False),          # Регистрозависимый поиск
    ('HELLO', 'o', False),          # Регистрозависимый поиск

    # Пробельные символы
    ('   ', ' ', True),             # Строка из пробелов
    ('\t\n\r', '\r', True),         # Различные пробельные символы

    # Граничные случаи
    ('a', 'a', True),               # Одиночный символ
    ('aa', 'a', True),              # Повторяющийся символ
    ('', 'a', False),               # Пустая строка
    (' ', '', True),                # Пустой символ в непустой строке
    ('\0', '\0', True),             # Нулевой символ
    ('abc\0def', '\0', False),      # Нулевой символ внутри строки
])
def test_end_with_positive(string_utils_instance, input_str, input_symbol, expected_bool):
    """
    Расширенное тестирование метода
    """
    assert string_utils_instance.end_with(input_str, input_symbol) == expected_bool


@pytest.mark.negative_test
@pytest.mark.parametrize('input_str, input_symbol, expected_result', [
    ('text', 'ab', False),      # Поиск подстроки вместо одного символа
])
def test_end_with_negative_values(string_utils_instance, input_str, input_symbol, expected_result):
    """
    Проверяет обработку некорректных входных данных, которые должны вернуть False
    """
    assert string_utils_instance.end_with(input_str, input_symbol) == expected_result


@pytest.mark.negative_test
@pytest.mark.parametrize('input_str, input_symbol, expected_error', [
    ('text', ['a'], TypeError),                 # Список в качестве символа
    ('text', 123, TypeError),                   # Число в качестве символа
    ('text', None, TypeError),                  # None в качестве символа
    ({'a': 1}, 'a', AttributeError),            # Словарь в качестве строки
    (True, 'a', AttributeError),                # Boolean в качестве строки
    (None, 'a', AttributeError),                # None в качестве строки
    (123, 'a', AttributeError),                 # Число в качестве строки
    ('text', object(), TypeError),              # Объект как символ
    ('text', float(1.0), TypeError),            # Float как символ
    (b'bytes', 'a', TypeError),                 # Bytes как строка
    (bytearray(b'text'), 'a', TypeError),       # Bytearray как строка
    (['a'], 'a', AttributeError),               # Список в качестве строки
])
def test_end_with_exceptions(string_utils_instance, input_str, input_symbol, expected_error):
    """
    Проверяет, что метод вызывает исключения при определенных некорректных входных данных
    """
    with pytest.raises(expected_error):
        string_utils_instance.end_with(input_str, input_symbol)


@pytest.mark.positive_test
def test_end_with_immutability(string_utils_instance):
    """
    Проверяет, что входные данные не изменяются
    """
    input_str = "Hello, World!"
    input_symbol = "o"
    original_str = input_str
    original_symbol = input_symbol

    string_utils_instance.end_with(input_str, input_symbol)

    assert input_str == original_str
    assert input_symbol == original_symbol


@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, input_symbol, expected_bool', [
    ('👨‍👩‍👧‍👦', '👦', True),    # Составной эмодзи
    ('🏳️‍🌈', '🌈', True),    # Эмодзи с модификатором
    ('👨🏻‍💻', '💻', True),    # Эмодзи с тоном кожи
])
def test_end_with_complex_unicode(string_utils_instance, input_str, input_symbol, expected_bool):
    """
    Проверяет работу с составными Unicode символами
    """
    assert string_utils_instance.end_with(input_str, input_symbol) == expected_bool


@pytest.mark.positive_test
@pytest.mark.parametrize('input_str, input_symbol, expected_bool', [
    (' \t\n\r\f\v', ' ', False),     # Все виды пробельных символов в начале строки
    (' \t\n\r\f\v', '\v', True),     # Все виды пробельных символов в конце строки
    ('\u2000', '\u2000', True),      # Unicode пробел
    ('\xa0', '\xa0', True),          # Non-breaking space
])
def test_end_with_whitespace(string_utils_instance, input_str, input_symbol, expected_bool):
    """
    Проверяет работу с различными видами пробельных символов
    """
    assert string_utils_instance.end_with(input_str, input_symbol) == expected_bool
