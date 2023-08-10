from components.header.es_club_logo import EsClubLogo
from components.header.fastlink import Fastlink
from locators.locators import Locators
from pages.base_page import BasePage



class Header(BasePage):
    fastlink = Fastlink()
    es_club_logo = EsClubLogo()

    def isVisible(self):
        return self.browser.find_element(*Locators.header.HEADER_COMMON).is_displayed()

