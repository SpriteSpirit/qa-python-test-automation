def is_year_leap(year):
    """
    Проверяет, является ли год високосным

    :param year: Год для проверки
    :return: True, если год високосный, False в противном случае
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(is_year_leap(2023))
