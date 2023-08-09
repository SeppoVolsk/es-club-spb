from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, browser, url):
        self.browser: WebDriver = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
