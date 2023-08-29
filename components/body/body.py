from selenium.webdriver.chrome.webdriver import WebDriver

from components.base_component import BaseComponent
from locators.locators import Locators


class Body(BaseComponent):
    def __init__(self, browser: WebDriver):
        super().__init__(
            browser,
            locator=Locators.body.BODY_COMMON,
            description="Средняя часть сайта (Body)")