from enum import Enum
from components.base_component import BaseComponent
from locators.locators import Locators
from resources.resources import Resources


class _FastlinkItems(Enum):
    about = "about/"
    about_media = "about/media/"
    about_otzyvy = "about/otzyvy/"
    about_workplace = "about/workplace/"
    about_sale_den_klienta = "about/sale/den_klienta/"
    about_3d = "about/3d/"


class FastLinkMenu(BaseComponent):
    def is_visible(self):
        return super().is_visible(Locators.header.FAST_LINK_MENU_COMMON)
    def check_fastlink_items_urls(self):
        for e in _FastlinkItems:
            self.browser.get(Resources.links.BASE_URL + e.value)
            yield self.browser.current_url

