from enum import Enum

from selenium.webdriver.common.by import By


class StoreSelector(Enum):
    """
    Класс для работы с CSS селекторами на странице Интернет-магазина
    """

    # LOGIN PAGE
    LOGIN_INPUT_NAME = (By.ID, 'user-name')
    LOGIN_INPUT_PASSWORD = (By.ID, 'password')
    LOGIN_SUBMIT_BUTTON = (By.ID, 'login-button')

    # SHOP PAGE
    ALL_INVENTORY_ITEMS_ON_PAGE = (By.CLASS_NAME, 'inventory_item')
    INPUT_FIELD = (By.CSS_SELECTOR, 'input.form_input')

    ITEM_NAME = (By.CSS_SELECTOR, 'div.inventory_item_name')
    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    ADD_ITEM_BUTTON = (By.CSS_SELECTOR, 'button.btn_inventory')
    CART_BUTTON = (By.CSS_SELECTOR, 'a.shopping_cart_link')

    # CART PAGE
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    # CHECKOUT FORM
    # FORM_GROUP = (By.CLASS_NAME, 'form_group')
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')

    # CHECKOUT OVERVIEW
    SUMMARY_LABEL = (By.CLASS_NAME, 'summary_total_label')
    SUMMARY_TAX_LABEL = (By.CLASS_NAME, 'summary_tax_label')
