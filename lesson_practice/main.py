from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")


login_input_field = driver.find_element(By.ID, 'user-name')
password_input_field = driver.find_element(By.ID, 'password')

login_input_field.clear()
password_input_field.clear()

login_button = driver.find_element(By.ID, 'login-button')

driver.implicitly_wait(5)
login_creds = driver.find_element(By.ID, 'login_credentials').text
login_pass = driver.find_element(By.CLASS_NAME, 'login_password').text

user_name = login_creds.split('\n')[1]
user_pass = login_pass.split('\n')[1]

user_data = {
    'user-name': user_name,
    'password': user_pass,
    'first-name': 'Angelina',
    'last-name': 'Khalueva',
    'zip-code': '190000',
}

login_input_field.send_keys(user_name)
password_input_field.send_keys(user_pass)
login_button.click()

inventory_list = WebDriverWait(driver, 10).until(
        ec.presence_of_all_elements_located((By.CLASS_NAME, 'inventory_item'))
    )

assert inventory_list, "Не удалось получить результат"

items_label = [card.find_element(By.CSS_SELECTOR, 'div.inventory_item_name') for card in inventory_list]

print([item.text for item in items_label])

for i in range(len(inventory_list)):

    if "backpack" in items_label[i].text.lower():
        inventory_list[i].find_element(By.CSS_SELECTOR, 'button.btn_inventory').click()
    elif "bolt t-shirt" in items_label[i].text.lower():
        inventory_list[i].find_element(By.CSS_SELECTOR, 'button.btn_inventory').click()
    elif "onesie" in items_label[i].text.lower():
        inventory_list[i].find_element(By.CSS_SELECTOR, 'button.btn_inventory').click()

cart_button = driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link')
cart_button.click()

checkout_button = driver.find_element(By.CSS_SELECTOR, '#checkout')
checkout_button.click()

# Ожидаем появления полей формы
first_name_field = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.ID, 'first-name'))
)
last_name_field = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.ID, 'last-name'))
)
zip_code_field = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.ID, 'postal-code'))
)

first_name_field.send_keys(user_data['first-name'])
last_name_field.send_keys(user_data['last-name'])
zip_code_field.send_keys(user_data['zip-code'])

continue_button = driver.find_element(By.CSS_SELECTOR, '#continue')
continue_button.click()

item_prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
total_price = sum(float(price.text.replace('$', '')) for price in item_prices)

total_tax = driver.find_element(By.CLASS_NAME, 'summary_tax_label')
total_tax_value = float(total_tax.text.split()[1].replace('$', ''))

summary_total_label = driver.find_element(By.CLASS_NAME, 'summary_total_label')
browser_cart_total_price = float(summary_total_label.text.split()[1].replace('$', ''))

total_price += total_tax_value


sleep(10)
assert browser_cart_total_price == total_price

# Закрываем драйвер
driver.quit()
