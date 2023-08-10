from enum import Enum
from pages.base_page import BasePage
from resources.resources import Resources


class _FastlinkItems(Enum):
    about = "about/"
    about_media = "about/media/"
    about_otzyvy = "about/otzyvy/"
    about_workplace = "about/workplace/"
    about_sale_den_klienta = "about/sale/den_klienta/"
    about_3d = "about/3d/"


class Fastlink(BasePage):
    def check_fastlink_items_urls(self):
        for e in _FastlinkItems:
            self.browser.get(Resources.links.BASE_URL + e.value)
            yield self.browser.current_url

