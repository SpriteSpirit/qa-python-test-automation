class Smartphone:
    """
    Смартфон.

    Attributes:
        brand (str): Марка телефона
        model (str): Модель телефона
        number (str): Номер телефона в формате +7XXXXXXXXxx (без кода страны)
    """
    brand: str
    model: str
    number: str

    def __init__(self, brand: str, model: str, number: str) -> object:
        self.brand = brand
        self.model = model
        self.number = "+7" + number

    def __str__(self):
        return f"{self.brand} - {self.model}. {self.number}"
