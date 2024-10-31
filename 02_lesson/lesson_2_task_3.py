from math import ceil


def square(side):
    """
    Вычисление площади квадрата
    :param side: Длина стороны квадрата
    :return: Площадь квадрата, округленная в большую сторону
    """
    return ceil(side ** 2)


print(square(2.3))
