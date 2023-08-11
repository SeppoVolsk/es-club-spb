from components.base_component import BaseComponent
from locators.locators import Locators


class EsClubLogo(BaseComponent):
    def is_visible(self):
        return super().is_visible(Locators.header.ES_CLUB_LOGO_COMMON)
