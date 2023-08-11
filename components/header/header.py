from components.base_component import BaseComponent
from components.header.header_parts.address_schedule_block import AddressScheduleBlock
from components.header.header_parts.beauty_salon_link import BeautySalonLink
from components.header.header_parts.body_menu import BodyMenu
from components.header.header_parts.es_club_logo import EsClubLogo
from components.header.header_parts.fast_link_menu import FastLinkMenu
from components.header.header_parts.phone_number_link import PhoneNumberLink
from components.header.header_parts.sale_link import SaleLink
from locators.locators import Locators




class Header(BaseComponent):
    def __init__(self, browser):
        super().__init__(browser)
        self.fast_link_menu = FastLinkMenu(browser)
        self.es_club_logo = EsClubLogo(browser)
        self.sale_link = SaleLink(browser)
        self.phone_number_link = PhoneNumberLink(browser)
        self.beauty_salon_link = BeautySalonLink(browser)
        self.body_menu = BodyMenu(browser)
        self.address_schedule_block = AddressScheduleBlock(browser)

    def is_visible(self):
        return super().is_visible(Locators.header.HEADER_COMMON)

