from selenium.webdriver.chrome.webdriver import WebDriver

from components.base_component import BaseComponent
from locators.locators import Locators


class Content(BaseComponent):
    def __init__(self, browser: WebDriver):
        super().__init__(
            browser,
            locator=Locators.header.HEADER_COMMON,
            description="Средняя часть сайта (body)")