from typing import List


class Calculator:
    a: float
    b: float
    num_list: List[float]

    def sum(self, a: float, b: float) -> float:
        """
        Возвращает сумму a и b
        """
        return a + b

    def sub(self, a: float, b: float) -> float:
        """
        Возвращает разницу a и b
        """
        return a - b

    def mul(self, a: float, b: float) -> float:
        """
        Возвращает произведение a и b
        """
        return a * b

    def div(self, a: float, b: float) -> float:
        """
        Возвращает отношение a и b
        """
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError("На ноль делить нельзя")

    def pow(self, a: float, b: float = 2) -> float:
        """
        Возвращает a в степени b
        """
        return a ** b

    def average(self, num_list: List[float]) -> float:
        """
        Возвращает среднее арифметическое num_list
        """
        if len(num_list) != 0:
            return self.div(sum(num_list), len(num_list))
        else:
            return 0
