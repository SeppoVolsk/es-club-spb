from enum import Enum
from components.base_component import BaseComponent
from components.clickable_component import ClickableComponent
from locators.locators import Locators
from resources.resources import Resources




class FastLinkMenu(BaseComponent):
    def __init__(self, browser):
        super().__init__(browser)
        self.about_item = ClickableComponent(locator=Locators.header.fast_link_menu.ABOUT,
                                        link=Resources.links.BASE_URL + Resources.links.ENDPOINT_ABOUT,
                                        description="О нас",
                                        browser=self.browser)
        self.about_media_item = ClickableComponent(locator=Locators.header.fast_link_menu.MEDIA,
                                              link=Resources.links.BASE_URL + Resources.links.ENDPOINT_ABOUT_MEDIA,
                                              description="Медиа",
                                              browser=self.browser)
        self.about_otzyvy_item = ClickableComponent(locator=Locators.header.fast_link_menu.OTZYVY,
                                               link=Resources.links.BASE_URL + Resources.links.ENDPOINT_ABOUT_OTZYVY,
                                               description="Отзывы",
                                               browser=self.browser)
        self.about_workplace_item = ClickableComponent(locator=Locators.header.fast_link_menu.WORKPLACE,
                                                  link=Resources.links.BASE_URL + Resources.links.ENDPOINT_ABOUT_WORKPLACE,
                                                  description="Аренда",
                                                  browser=self.browser)
        self.about_sale_den_klienta_item = ClickableComponent(locator=Locators.header.fast_link_menu.SALE_DEN_KLIENTA,
                                                         link=Resources.links.BASE_URL + Resources.links.ENDPOINT_ABOUT_SALE_DEN_KLIENTA,
                                                         description="День клиента",
                                                         browser=self.browser)
        self.about_3d_item = ClickableComponent(locator=Locators.header.fast_link_menu.TOUR_3D,
                                           link=Resources.links.BASE_URL + Resources.links.ENDPOINT_ABOUT_3D,
                                           description="3d тур",
                                           browser=self.browser)

    def is_visible(self):
        return super().is_visible(Locators.header.FAST_LINK_MENU_COMMON)
