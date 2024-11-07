class User:
    """
    Пользователь.

    Attributes:
        first_name (str): Имя пользователя.
        last_name (str): Фамилия пользователя.
    """
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str) -> object:
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self) -> None:
        """
        Выводит имя пользователя.
        """
        print(f"First name: {self.first_name}")

    def print_last_name(self) -> None:
        """
        Выводит фамилию пользователя.
        """
        print(f"Last name: {self.last_name}")

    def print_full_name(self) -> None:
        """
        Выводит полное имя пользователя.
        """
        print(f"Full name: {self.first_name}")
