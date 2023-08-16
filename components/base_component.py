from selenium.webdriver.chrome.webdriver import WebDriver

from logger.logger import l


class BaseComponent:
    def __init__(self, browser=None):
        self.browser: WebDriver = browser

    def is_visible(self, *args):
        return self.browser.find_element(*args[0]).is_displayed()

    def is_on_page(self, *args):
        is_on_page = True
        try:
            self.browser.find_element(*args[0])
        except Exception as err:
            l.error("ЭЛЕМЕНТ НЕ НАЙДЕН НА СТРАНИЦЕ!")
            is_on_page = False
        return is_on_page


