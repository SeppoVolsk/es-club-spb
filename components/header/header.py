from components.base_component import BaseComponent
from locators.locators import Locators


class Header(BaseComponent):
    def __init__(self, browser,
                 fast_link_menu=None,
                 body_menu=None,
                 address_schedule_block=None,
                 sale_link=None,
                 es_club_logo=None,
                 beauty_salon_link=None,
                 phone_number_link=None):
        super().__init__(browser)
        self.fast_link_menu = fast_link_menu
        self.body_menu = body_menu
        self.address_schedule_block = address_schedule_block
        self.sale_link = sale_link
        self.es_club_logo = es_club_logo
        self.beauty_salon_link = beauty_salon_link
        self.phone_number_link = phone_number_link


    def is_exists(self):
        return super().is_exists(Locators.header.HEADER_COMMON)

    def is_visible(self):
        return super().is_visible(Locators.header.HEADER_COMMON)
