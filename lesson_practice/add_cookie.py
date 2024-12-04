from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}

driver.get("https://www.labirint.ru/")

# добавить куки
driver.add_cookie(my_cookie)

# получить все куки
all_cookie = driver.get_cookies()
print(all_cookie)

# обновить страницу
driver.refresh()

# удалить все куки
driver.delete_all_cookies()
driver.refresh()

sleep(5)
driver.quit()
