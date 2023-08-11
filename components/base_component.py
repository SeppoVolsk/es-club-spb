from selenium.webdriver.chrome.webdriver import WebDriver


class BaseComponent:
    def __init__(self, browser=None):
        self.browser: WebDriver = browser

    def is_visible(self, *args):
        return self.browser.find_element(*args[0]).is_displayed()
