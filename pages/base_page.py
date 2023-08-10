from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver

class BasePage:
    def __init__(self, browser=webdriver.Chrome(), url=None):
        self.browser: WebDriver = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        return self
