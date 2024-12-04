from time import sleep
from selenium import webdriver

# Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
# Edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def make_screenshot(browser):  # определили единый метод
    browser.maximize_window()
    browser.get("https://ya.ru/")
    sleep(5)
    browser.save_screenshot("./ya.png")
    browser.quit()


chrome = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

firefox = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))

edge = webdriver.Edge(service=EdgeService(
    EdgeChromiumDriverManager().install()))

make_screenshot(chrome)
make_screenshot(firefox)
make_screenshot(edge)