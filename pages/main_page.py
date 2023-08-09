from selenium.webdriver.common.by import By

from locators.main_page_locators import MainPageLocators
from resources.resources import Resources
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_uslugi_tab(self):
        uslugi_tab_link = self.browser.find_element(*MainPageLocators.BODY_TABS_USLUGI)
        uslugi_tab_link.click()

    def should_be_phone_number(self):
        assert self.browser.find_element(*MainPageLocators.HEADER_PHONE_NUMBER), (
            Resources.strings.ERROR_NO_PHONE)
