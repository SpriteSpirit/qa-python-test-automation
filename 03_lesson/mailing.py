from address import Address


class Mailing:
    """
    Отправка письма/посылки.
    Содержит информацию о отправителе и получателе, стоимости и треку отправки.

    Attributes:
        to_address (Address): кому
        from_address (Address): от кого
        cost (float): стоимость
        track (str): трек отслеживания
    """
    to_address: Address
    from_address: Address
    cost: float
    track: str

    def __init__(self, to_address: Address, from_address: Address, cost: float, track: str) -> object:
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} "
                f"из "
                f"{self.from_address.zipcode}, {self.from_address.city}, {self.from_address.street}, "
                f"{self.from_address.house_number} - {self.from_address.apartment_number} "
                f"в "
                f"{self.to_address.zipcode}, {self.to_address.city}, "
                f"{self.to_address.house_number} - {self.to_address.apartment_number}. "
                f"Стоимость {self.cost} рублей.")
