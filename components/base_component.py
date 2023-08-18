from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver

from app_error._app_error import E
from logger.logger import l


class BaseComponent:
    def __init__(self,
                 browser: WebDriver | None,
                 locator: str | None,
                 description: str | None = None,
                 ):
        self.browser = browser
        self.locator = locator
        self.description = description

    def is_visible(self):
        return self.browser.find_element(*self.locator).is_displayed()

    def is_exists(self):
        is_on_page = True
        try:
            self.browser.find_element(self.locator)
        except Exception as err:
            l.error(E.message(err))
            is_on_page = False
        return is_on_page
