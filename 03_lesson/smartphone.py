class Smartphone:
    brand: str
    model: str
    number: str

    def __init__(self, brand, model, number):
        self.brand: str = brand
        self.model: str = model
        self.number: str = "+7" + number

    def __str__(self):
        return f"{self.brand} - {self.model}. {self.number}"
