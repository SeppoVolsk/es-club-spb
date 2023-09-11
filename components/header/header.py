from selenium.webdriver.chrome.webdriver import WebDriver

from components.base_component import BaseComponent
from components.clickable_component import ClickableComponent
from locators.locators import Locators


class Header(BaseComponent):
    def __init__(self, browser: WebDriver | None,
                 fast_menu: dict[str:ClickableComponent] | None = None,
                 body_menu: dict[str:ClickableComponent] | None = None,
                 address_schedule_block: list[BaseComponent] | None = None,
                 sale_link: ClickableComponent | None = None,
                 es_club_logo: ClickableComponent | None = None,
                 beauty_salon_link: ClickableComponent | None = None,
                 phone_number_link: ClickableComponent | None = None,
                 search_row: list[BaseComponent, ClickableComponent] | None = None,
                 route_string: dict[str:BaseComponent] | None = None):
        super().__init__(browser,
                         locator=Locators.header.HEADER_COMMON,
                         description="Верхняя часть сайта (Header)")
        self.fast_menu = fast_menu
        self.body_menu = body_menu
        self.address_schedule_block = address_schedule_block
        self.sale_link = sale_link
        self.es_club_logo = es_club_logo
        self.beauty_salon_link = beauty_salon_link
        self.phone_number_link = phone_number_link
        self.search_field = search_row
        self.route_string = route_string
