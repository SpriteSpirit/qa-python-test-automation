from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу
url = 'http://the-internet.herokuapp.com/add_remove_elements/'
driver.get(url)

# Найти кнопку
button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

# Пять раз кликнуть на кнопку Add Element
for i in range(5):
    button.click()

# Собрать со страницы список кнопок Delete
elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.added-manually'))
)

# Вывести на экран размер списка
print(f'{len(elements)=}')

# Ожидание 10 сек
sleep(10)

# Закрытие браузера
driver.quit()
