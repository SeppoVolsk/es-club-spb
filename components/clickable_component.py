from selenium.webdriver.chrome.webdriver import WebDriver

from components.base_component import BaseComponent


class ClickableComponent(BaseComponent):
    def __init__(self,
                 browser: WebDriver | None,
                 locator: str | None,
                 description: str | None = None,
                 link: str | None = None
                 ):
        super().__init__(browser, locator, description)
        self.link = link

    def click(self):
        self.browser.find_element(*self.locator).click()

