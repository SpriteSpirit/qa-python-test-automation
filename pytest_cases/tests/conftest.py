import os
from pytest_cases.src.calculator import Calculator
import pytest
import json


# Проверка существования файла
file_path = r'C:\Users\Angelina\PycharmProjects\qa-python-test-automation\pytest_cases\tests\fixtures\calculator_test_data.json'

if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")

# Загрузка параметров из JSON-файла
with open(file_path, 'r', encoding='utf-8') as file:
    test_data = json.load(file)


@pytest.fixture
def calculator_instance():
    """
    Фикстура, создающая экземпляр класса pytest_cases
    """
    return Calculator()


@pytest.fixture(params=test_data['sub_cases'])
def sub_cases(request):
    """
    Фикстура с различными вариантами вычитания
    """
    return request.param


@pytest.fixture(params=test_data['sum_cases'])
def sum_cases(request):
    """
    Фикстура с различными вариантами сложения
    """
    return request.param


@pytest.fixture(params=test_data['mul_cases'])
def mul_cases(request):
    """
    Фикстура с различными вариантами умножения
    """
    return request.param


@pytest.fixture(params=test_data['div_cases'])
def div_cases(request):
    """
    Фикстура с различными вариантами деления
    """
    return request.param
