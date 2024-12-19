from utilities.logger_utils import logger
from lesson_07.online_store_pages.main_page import StorePage
from lesson_07.online_store_pages.store_page_enum_selectors import StoreSelector as selector


class LoginPage(StorePage):
    """
    Page Object для страницы авторизации Интернет-магазина.
    """

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, login_data: dict) -> None:
        """
        Авторизоваться в системе.
        """

        logger.debug('Ввод логина и пароля')

        name = self.wait_presence_of_element(selector.LOGIN_INPUT_NAME.value)
        password = self.wait_presence_of_element(selector.LOGIN_INPUT_PASSWORD.value)

        name.clear()
        password.clear()

        name.send_keys(login_data['login'])
        password.send_keys(login_data['password'])

        submit_button = self.wait_presence_of_element(selector.LOGIN_SUBMIT_BUTTON.value)
        submit_button.click()

        logger.debug('Авторизация прошла успешно')

    # TODO: по-хорошему нужно разбить login на отдельные методы:
    #  очищение полей ввода,
    #  заполнение полей ввода,
    #  подтверждение
