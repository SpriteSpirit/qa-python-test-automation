from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


driver = webdriver.Edge(service=EdgeService(
    EdgeChromiumDriverManager().install()))
driver.get("https://ya.ru/")

element = driver.find_element(By.CSS_SELECTOR, "#text")
print(element) # (session="32e7dc49c21996914159dabff302c06d",
# element="f.85979FECF2BB7C3C58F97E54331AECA6.d.BF282807DC80E99A1E8B32198BB535E7.e.139")

element.clear()
sleep(3)
element.send_keys("Testing")

tag_link = driver.find_element(By.CSS_SELECTOR, "a[aria-label*='USD']").tag_name
text_link = driver.find_element(By.CSS_SELECTOR, "a[aria-label*='USD']").text
id_link = driver.find_element(By.CSS_SELECTOR, "a[aria-label*='USD']").id
print(text_link)
sleep(3)
# driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
# sleep(3)

sleep(5)
driver.quit()
