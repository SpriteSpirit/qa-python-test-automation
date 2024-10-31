def month_to_season(month: int):
    """
    Преобразует месяц в сезон
    :param month: int, месяц в году (от 1 до 12)
    :return: str, сезон
    """

    if month in range(1, 3) or month == 12:
        season = 'Зима'
    elif month in range(3, 6):
        season = 'Весна'
    elif month in range(6, 9):
        season = 'Лето'
    elif month in range(9, 12):
        season = 'Осень'
    else:
        return 'Неизвестный месяц'

    return season


print(month_to_season(10))
