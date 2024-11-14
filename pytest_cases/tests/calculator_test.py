import pytest


def test_sum(calculator_instance, sum_cases):
    a, b, expected = sum_cases
    result = calculator_instance.sum(a, b)
    assert round(result, 2) == expected


def test_sub(calculator_instance, sub_cases):
    a, b, expected = sub_cases
    result = calculator_instance.sub(a, b)
    assert round(result, 2) == expected


def test_mul(calculator_instance, mul_cases):
    a, b, expected = mul_cases
    result = calculator_instance.mul(a, b)
    assert round(result, 2) == expected


def test_div(calculator_instance, div_cases):
    a, b, expected = div_cases
    result = calculator_instance.div(a, b)
    assert round(result, 2) == expected


@pytest.mark.positive_test
def test_div_zero(calculator_instance):
    with pytest.raises(ZeroDivisionError):
        calculator_instance.div(10.0, 0.0)


@pytest.mark.skip(reason='Нет фикстур')
def test_pow(calculator_instance):
    assert calculator_instance.pow(10.0, 5.0) == 100000.0  # 10^5


@pytest.mark.parametrize('num, result', [
    (2, 4),
    (-5, 25),
    (2.5, 6.25),
    (0, 0),
])
def test_pow_default(calculator_instance, num, result):
    assert calculator_instance.pow(num) == result


def test_average(calculator_instance):
    assert calculator_instance.average([1.0, 2.0, 3.0, 4.0, 5.0]) == 3.0


def test_average_empty_list(calculator_instance):
    assert calculator_instance.average([]) == 0.0
