from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.labirint.ru/")
search_locator = "#search-field"

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("Python", Keys.RETURN)

book_locator = "div.product-card"
books = driver.find_elements(By.CSS_SELECTOR, book_locator)

print(len(books))  # 60

for book in books:
    author = "product-card__author"
    price = 'product-card__price-current'
    title = 'product-card__name'

    try:
        author = book.find_element(By.CSS_SELECTOR, f'div.{author}').text
        price = book.find_element(By.CSS_SELECTOR, f'div.{price}').text
        title = book.find_element(By.CSS_SELECTOR, f'a.{title}').text
    except:
        author = "Не указан"
        price = "Не указан"
        title = "Не указан"

    print(f"{author}\t{title}\t{price}\t")

sleep(5)
driver.quit()
