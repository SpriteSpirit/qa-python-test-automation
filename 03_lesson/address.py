class Address:
    """
    Адрес.

    Attributes:
        zipcode (int): индекс
        city (str): город
        street (str): улица
        house_number (int): номер дома
        apartment_number (int): номер квартиры
    """
    zipcode: int
    city: str
    street: str
    house_number: int
    apartment_number: int

    def __init__(self, zipcode: int, city: str, street: str, house_number: int, apartment_number: int) -> object:
        self.zipcode = zipcode
        self.city = city
        self.street = street
        self.house_number = house_number
        self.apartment_number = apartment_number
