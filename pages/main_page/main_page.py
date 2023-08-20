from selenium.webdriver.chrome.webdriver import WebDriver

from components.content.content import Content
from components.footer.footer import Footer
from components.header.header import Header
from locators.locators import Locators
from pages.base_page import BasePage
from resources.resources import Resources


class MainPage(BasePage):
    def __init__(self, browser: WebDriver):
        super().__init__(browser, url=Resources.links.BASE_URL)
        self.header = Header(browser)
        self.content = Content(browser)
        self.footer = Footer(browser)
