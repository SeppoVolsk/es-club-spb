from enum import Enum
from components.base_component import BaseComponent
from locators.locators import Locators
from resources.resources import Resources



class SaleLink(BaseComponent):
    def is_visible(self):
        return super().is_visible(Locators.header.SALE_LINK_COMMON)


