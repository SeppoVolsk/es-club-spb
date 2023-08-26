import pytest

from components.clickable_component import ClickableComponent
from locators.locators import Locators
from resources.resources import R

@pytest.fixture(scope="session")
def items():
    class Item:
        (ABOUT,
         MEDIA,
         OTZYVY,
         WORKPLACE,
         DEN_KLIENTA,
         TOUR_3D) = range(6)
    return Item()

@pytest.fixture()
def fast_link_menu(header, items, browser):
    about = ClickableComponent(locator=Locators.header.fast_link_menu.ABOUT,
                               link=R.links.BASE_URL + R.links.ENDPOINT_ABOUT,
                               description="О нас",
                               browser=browser)
    media = ClickableComponent(locator=Locators.header.fast_link_menu.MEDIA,
                               link=R.links.BASE_URL + R.links.ENDPOINT_ABOUT_MEDIA,
                               description="Медиа",
                               browser=browser)
    otzyvy = ClickableComponent(locator=Locators.header.fast_link_menu.OTZYVY,
                                link=R.links.BASE_URL + R.links.ENDPOINT_ABOUT_OTZYVY,
                                description="Отзывы",
                                browser=browser)
    workplace = ClickableComponent(locator=Locators.header.fast_link_menu.WORKPLACE,
                                   link=R.links.BASE_URL + R.links.ENDPOINT_ABOUT_WORKPLACE,
                                   description="Аренда",
                                   browser=browser)
    den_klienta = ClickableComponent(locator=Locators.header.fast_link_menu.SALE_DEN_KLIENTA,
                                     link=R.links.BASE_URL + R.links.ENDPOINT_ABOUT_SALE_DEN_KLIENTA,
                                     description="День клиента",
                                     browser=browser)
    tour_3d = ClickableComponent(locator=Locators.header.fast_link_menu.TOUR_3D,
                                 link=R.links.BASE_URL + R.links.ENDPOINT_ABOUT_3D,
                                 description="3d тур",
                                 browser=browser)

    header.fast_link_menu = {
        items.ABOUT: about,
        items.MEDIA: media,
        items.OTZYVY: otzyvy,
        items.WORKPLACE: workplace,
        items.DEN_KLIENTA: den_klienta,
        items.TOUR_3D: tour_3d}
