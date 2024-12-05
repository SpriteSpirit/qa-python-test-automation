from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_swag_labs_checkout(driver):
    total_price = 0

    # Открываем сайт
    driver.get("https://www.saucedemo.com/")

    # Получаем логин и пароль
    login_creds = driver.find_element(By.ID, 'login_credentials').text
    login_pass = driver.find_element(By.CLASS_NAME, 'login_password').text
    user_name = login_creds.split('\n')[1]
    user_pass = login_pass.split('\n')[1]

    # Логинимся
    driver.find_element(By.ID, 'user-name').send_keys(user_name)
    driver.find_element(By.ID, 'password').send_keys(user_pass)
    driver.find_element(By.ID, 'login-button').click()

    # Проверяем, что страница загружена, получая список товаров
    inventory_list = WebDriverWait(driver, 10).until(
        ec.presence_of_all_elements_located((By.CLASS_NAME, 'inventory_item'))
    )
    assert inventory_list, "Не удалось загрузить список товаров"

    # Добавляем определенные товары в корзину и считаем стоимость
    items_to_add = ["sauce labs backpack", "sauce labs bolt t-shirt", "sauce labs onesie"]

    for item in inventory_list:
        item_name = item.find_element(By.CSS_SELECTOR, 'div.inventory_item_name').text.lower()

        if any(product == item_name for product in items_to_add):
            item_price = item.find_element(By.CLASS_NAME, 'inventory_item_price').text.replace('$', '')
            total_price += float(item_price)
            item.find_element(By.CSS_SELECTOR, 'button.btn_inventory').click()
            print(f"Добавлен товар: {item_name}, цена: ${item_price}")

    # Переходим в корзину
    driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    # Нажимаем кнопку Checkout
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    # Заполняем форму
    user_data = {
        'first-name': 'Angelina',
        'last-name': 'Khalueva',
        'zip-code': '190000',
    }
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'first-name'))).send_keys(user_data['first-name'])

    driver.find_element(By.ID, 'last-name').send_keys(user_data['last-name'])
    driver.find_element(By.ID, 'postal-code').send_keys(user_data['zip-code'])
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    # Проверяем итоговую сумму
    summary_label = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    summary_tax_label = driver.find_element(By.CLASS_NAME, 'summary_tax_label').text

    total_cart_price = float(summary_label.split()[1].replace('$', ''))
    total_tax = float(summary_tax_label.split()[1].replace('$', ''))

    # Проверяем, что итоговая сумма совпадает
    assert total_cart_price == total_price + total_tax, "Итоговая сумма не совпадает"
