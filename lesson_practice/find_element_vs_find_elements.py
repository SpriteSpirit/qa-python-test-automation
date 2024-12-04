from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/checkboxes")

# find_element ищет первый элемент
div = driver.find_element(By.CSS_SELECTOR, "#page-footer")
a_attr = div.find_element(By.CSS_SELECTOR, "a")

print(a_attr.get_attribute("href"))

# find_elements все элементы
all_div = driver.find_elements(By.CSS_SELECTOR, "div")
length = len(all_div)
print(f"Количество div-элементов: {length}")
print(f'div-элемент: {all_div[2].text}')

sleep(3)
driver.quit()
