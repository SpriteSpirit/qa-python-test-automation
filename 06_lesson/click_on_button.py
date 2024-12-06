from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)

# Перейти на сайт
driver.get("http://uitestingplayground.com/ajax")

# Нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

# Получить текст из зеленой плашки
content = driver.find_element(By.CSS_SELECTOR, '#content')
p_text = content.find_element(By.CSS_SELECTOR, 'p.bg-success').text

# Вывести в консоль текст
print(p_text)
