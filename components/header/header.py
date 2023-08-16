from components.base_component import BaseComponent
from components.clickable_component import ClickableComponent
from components.header.parts.address_schedule_block import AddressScheduleBlock
from components.header.parts.body_menu import BodyMenu
from components.header.parts.fast_link_menu import FastLinkMenu
from locators.locators import Locators
from resources.resources import Resources


class Header(BaseComponent):
    def __init__(self, browser):
        super().__init__(browser)
        self.fast_link_menu = FastLinkMenu(browser)
        self.body_menu = BodyMenu(browser)
        self.address_schedule_block = AddressScheduleBlock(browser)
        self.sale_link = ClickableComponent(locator=Locators.header.SALE_LINK_COMMON,
                                            link=Resources.links.BASE_URL + Resources.links.ENDPOINT_SALE,
                                            description="Ссылка Акции в красном квадрате",
                                            browser=browser)
        self.es_club_logo = ClickableComponent(locator=Locators.header.ES_CLUB_LOGO_COMMON,
                                               link=Resources.links.BASE_URL,
                                               description="Логотип ES Club",
                                               browser=browser)
        self.beauty_salon_link = ClickableComponent(locator=Locators.header.BEAUTY_SALON_COMMON,
                                                    link=Resources.links.BASE_URL,
                                                    description='Надпись "Салон Красоты"',
                                                    browser=browser)
        self.phone_number_link = ClickableComponent(locator=Locators.header.PHONE_NUMBER,
                                                    link="tel:88124673030",
                                                    description='Надпись "+78124673030"',
                                                    browser=browser)

    @property
    def current_url(self):
        return self.browser.current_url

    def is_on_page(self):
        return super().is_on_page(Locators.header.HEADER_COMMON)

    def is_visible(self):
        return super().is_visible(Locators.header.HEADER_COMMON)
