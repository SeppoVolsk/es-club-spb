from components.header.header import Header
from locators.locators import Locators
from pages.base_page import BasePage


class MainPage(BasePage):




    def go_to_uslugi_tab(self):
        uslugi_tab_link = self.browser.find_element(*Locators.main_page.BODY_TABS_USLUGI)
        uslugi_tab_link.click()
        return self

    def should_be_phone_number(self):
        return self.browser.find_element(*Locators.main_page.PHONE_NUMBER).text

