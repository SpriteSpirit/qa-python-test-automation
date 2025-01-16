from utilities.logger_utils import logger
from lesson_07.online_store_pages.store_page_enum_selectors import StoreSelector as selector
from lesson_07.online_store_pages.main_page import StorePage
import allure


class ItemPage(StorePage):
    """
    Page Object для страницы c товарами.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'inventory.html'

    @allure.step("Открытие страницы с товарами")
    def open_items_page(self):
        """
        Открывает страницу с товарами.
        """

        super().open(relative_url=self.url)

    @allure.step("Добавление товаров в корзину")
    def add_item_to_cart(self, item_list: list) -> float:
        """
        Добавляет товары в корзину.
        Возвращает стоимость всех товаров
        """

        all_items = self.wait_presence_of_elements(selector.ALL_INVENTORY_ITEMS_ON_PAGE.value)
        total_price = 0

        for item in all_items:
            item_name = item.find_element(*selector.ITEM_NAME.value).text.lower()

            if any(product == item_name for product in item_list):
                item_price = item.find_element(*selector.ITEM_PRICE.value).text.replace('$', '')
                total_price += float(item_price)
                item.find_element(*selector.ADD_ITEM_BUTTON.value).click()

                logger.debug(f'Товар добавлен в корзину: {item_name}, цена: ${item_price}')

        logger.debug(f'Все товары из списка добавлены в корзину. Общая стоимость: ${total_price}')
        return total_price

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переход в корзину.
        """

        cart_button = self.wait_presence_of_element(selector.CART_BUTTON.value)
        cart_button.click()
