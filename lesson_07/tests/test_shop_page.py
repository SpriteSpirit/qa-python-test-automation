import allure

from lesson_07.online_store_pages.checkout_page import CheckoutPage
from lesson_07.online_store_pages.items_page import ItemPage
from lesson_07.online_store_pages.login_page import LoginPage
from utilities.logger_utils import logger


@allure.title("Store page test")
@allure.tag("web")
@allure.label("owner", "khalueva.angelina")
@allure.story("Store page")
@allure.description("""
Проверяет добавление товаров в корзину, 
оформление заказа и подсчет стоимости
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_page(chrome_driver, mock_login_data, mock_items_data, mock_input_order_data):
    """
    Тестирование заполнения и отправки формы.
    """

    with allure.step("Создание экземпляра LoginPage"):
        logger.debug("Создание экземпляра LoginPage")
        login_page = LoginPage(chrome_driver)

    with allure.step("Открытие страницы"):
        logger.debug("Открытие страницы")
        login_page.open()

    with allure.step("Проверка, что страница авторизации открылась правильно"):
        current_url = chrome_driver.current_url
        expected_url = login_page.base_url

        assert current_url == expected_url, (f"Открыта неверная страница. Ожидалось: {expected_url}, "
                                             f"фактически: {current_url}")

    with allure.step("Авторизация на странице"):
        logger.debug("Авторизация на странице")
        login_page.login(mock_login_data)

    with allure.step("Создание экземпляра ItemPage"):
        logger.debug("Создание экземпляра ItemPage")
        items_page = ItemPage(chrome_driver)

    with allure.step("Проверка, что страница с товарами открылась правильно"):
        current_url = chrome_driver.current_url
        expected_url = f"{items_page.base_url}{items_page.url}"

        assert current_url == expected_url, (f"Открыта неверная страница. Ожидалось: {expected_url}, "
                                             f"фактически: {current_url}")

    with allure.step("Добавление товаров в корзину"):
        logger.debug("Добавление товаров в корзину")
        total_added_items_price = items_page.add_item_to_cart(mock_items_data)

    with allure.step("Переход в корзину"):
        logger.debug("Переход в корзину")
        items_page.go_to_cart()

    with allure.step("Создание экземпляра CartPage"):
        logger.debug("Создание экземпляра CartPage")
        checkout_page = CheckoutPage(chrome_driver)

    with allure.step("Проверка, что страница с товарами открылась правильно"):
        logger.debug("Проверка, что страница с товарами открылась правильно")
        current_url = chrome_driver.current_url
        expected_url = f"{checkout_page.base_url}{checkout_page.url}"

        assert current_url == expected_url, (f"Открыта неверная страница. Ожидалось: {expected_url}, "
                                             f"фактически: {current_url}")

    with allure.step("Открыть страницу оформления заказа"):
        logger.debug("Открыть страницу оформления заказа")
        checkout_page.start_checkout()

    with allure.step("Проверка, что страница оформления заказа открылась правильно"):
        logger.debug("Проверка, что страница оформления заказа открылась правильно")
        current_url = chrome_driver.current_url
        expected_url = f"{checkout_page.base_url}checkout-step-one.html"

        assert current_url == expected_url, (f"Открыта неверная страница. Ожидалось: {expected_url}, "
                                             f"фактически: {current_url}")

    with allure.step("Заполнение полей данными"):
        logger.debug("Заполнение полей данными")
        checkout_page.fill_checkout_form(mock_input_order_data)

    with allure.step("Получение итоговой суммы заказа"):
        logger.debug("Получение итоговой суммы заказа")
        total_cart_price, total_tax = checkout_page.get_summary_totals()

        assert total_cart_price == total_added_items_price + total_tax, \
            (f"Итоговая сумма не совпадает. Ожидалось: {total_added_items_price + total_tax}, "
             f"Получено: {total_cart_price}")
# TODO: можно сравнить кол-во товаров в корзине и кол-во товаров из мока
