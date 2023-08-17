from selenium.webdriver.chrome.webdriver import WebDriver

from components.base_component import BaseComponent


class ClickableComponent(BaseComponent):
    def __init__(self, locator, link, description, browser):
        super().__init__(browser=browser)
        self.locator = locator
        self.link = link
        self.description = description


    def click(self):
        self.browser.find_element(*self.locator).click()


    def is_visible(self):
        return super().is_visible(self.locator)
