from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage():

    def __init__(self, browser, url=None):
        self.browser: WebDriver = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        return self
