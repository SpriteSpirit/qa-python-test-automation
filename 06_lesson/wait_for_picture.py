from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)

# Перейти на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# явное ожидание изображения
WebDriverWait(driver, 30, 0.1).until(
    ec.presence_of_element_located(
        (By.CSS_SELECTOR, '#landscape')
    )
)

# Найти изображение
img = driver.find_element(By.CSS_SELECTOR, '#landscape')

# Получить значение атрибута src у изображения
src_text = img.get_attribute("src")

# Вывести в консоль значение атрибута
print(src_text)
