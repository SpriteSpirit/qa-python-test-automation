from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://chrome.google.com")
driver.get("https://vk.com")
#
# for i in range(1, 10):
#     driver.back()
#     driver.forward()
# driver.refresh()
driver.save_screenshot('./image.png')

sleep(20)
driver.quit()
