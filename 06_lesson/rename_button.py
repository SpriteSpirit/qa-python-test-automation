from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Перейти на сайт
driver.get("http://uitestingplayground.com/textinput")

# Найти поле ввода текста
input_field = driver.find_element(By.CSS_SELECTOR, '#newButtonName')

# Очистить поле
input_field.clear()

# Заполнить поле текстом SkyPro
input_field.send_keys("SkyPro")

# Нажать на синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
blue_button.click()

# Получить текст кнопки
button_text = blue_button.text

# Вывести в консоль текст
print(button_text)
