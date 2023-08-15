from components.base_component import BaseComponent
from locators.locators import Locators


class BodyMenu(BaseComponent):

    def is_visible(self):
        return super().is_visible(Locators.header.BODY_MENU_COMMON)