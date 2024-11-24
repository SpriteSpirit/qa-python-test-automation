import pytest
from pytest_cases.src.string_processor import StringProcessor


@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, expected_text', [
    ('test', 'Test.'),
    ('milk', 'Milk.'),
    ('Nice', 'Nice.'),
    ('Good.', 'Good.'),
    ('bye friend.', 'Bye friend.'),
])
def test_process(input_text, expected_text):
    assert StringProcessor.process(input_text) == expected_text


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text, expected_text', [
    ('1test', '1test.'),
    (' milk', ' milk.'),
    ('bBool', 'BBool.'),
    ('❌.', '❌.'),
    ('123', '123.'),
    ('', '.'),
    (' ', ' .'),
])
def test_process(input_text, expected_text):
    assert StringProcessor.process(input_text) == expected_text
