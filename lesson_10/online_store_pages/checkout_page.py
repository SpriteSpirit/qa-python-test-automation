from typing import Tuple

from lesson_07.online_store_pages.store_page_enum_selectors import StoreSelector as selector
from lesson_07.online_store_pages.main_page import StorePage
from utilities.logger_utils import logger
import allure


class CheckoutPage(StorePage):
    """
    Страница оформления заказа в магазине.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'cart.html'

    @allure.step("Открытие страницы с товарами")
    def open_cart_page(self):
        """
        Открывает страницу с товарами.
        """

        super().open(relative_url=self.url)

    @allure.step("Открытие страницы оформления заказа")
    def start_checkout(self) -> None:
        """
        Открывает страницу оформления заказа.
        """

        checkout_button = self.wait_presence_of_element(selector.CHECKOUT_BUTTON.value)
        checkout_button.click()

    @allure.step("Заполнение полей формы оформления заказа")
    def fill_checkout_form(self, user_data: dict) -> None:
        """
        Заполняет поля формы данными пользователя.
        """

        logger.info("Заполнение полей данными")

        first_name = self.wait_presence_of_element(selector.FIRST_NAME_INPUT.value)
        first_name.send_keys(user_data['first-name'])

        last_name = self.wait_presence_of_element(selector.LAST_NAME_INPUT.value)
        last_name.send_keys(user_data['last-name'])

        zip_code = self.wait_presence_of_element(selector.POSTAL_CODE_INPUT.value)
        zip_code.send_keys(user_data['postal-code'])

        continue_button = self.wait_presence_of_element(selector.CONTINUE_BUTTON.value)
        continue_button.click()
        logger.debug("Поля формы заполнены")

    @allure.step("Получение итоговой суммы корзины и налогов")
    def get_summary_totals(self) -> Tuple[float, float]:
        """
        Получает итоговую сумму корзины и налоги.
        """

        summary_label = self.wait_presence_of_element(selector.SUMMARY_LABEL.value)
        summary_tax_label = self.wait_presence_of_element(selector.SUMMARY_TAX_LABEL.value)
        total_cart_price = float(summary_label.text.split()[1].replace('$', ''))
        total_tax = float(summary_tax_label.text.split()[1].replace('$', ''))

        return total_cart_price, total_tax
