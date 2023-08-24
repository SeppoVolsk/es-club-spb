import pytest

from components.clickable_component import ClickableComponent
from locators.locators import Locators
from resources.resources import R

@pytest.fixture(scope="session")
def items():
    class Item:
        (MAIN,
         USLUGI,
         MASTERS,
         PORTFOLIO,
         CONTACTS,
         WRITE_TO) = range(6)
    return Item()

@pytest.fixture()
def body_menu(header, items):
    main = ClickableComponent(locator=Locators.header.body_menu.MAIN,
                               link=R.links.BASE_URL,
                               description="ГЛАВНАЯ",
                               browser=browser)
    uslugi = ClickableComponent(locator=Locators.header.body_menu.USLUGI,
                               link=R.links.BASE_URL + R.links.ENDPOINT_USLUGI,
                               description="УСЛУГИ",
                               browser=browser)
    masters = ClickableComponent(locator=Locators.header.body_menu.MASTERS,
                                link=R.links.BASE_URL + R.links.ENDPOINT_MASTERS,
                                description="МАСТЕРА",
                                browser=browser)
    portfolio = ClickableComponent(locator=Locators.header.body_menu.PORTFOLIO,
                                   link=R.links.BASE_URL + R.links.ENDPOINT_PORTFOLIO,
                                   description="НАШИ РАБОТЫ",
                                   browser=browser)
    contacts = ClickableComponent(locator=Locators.header.body_menu.CONTACTS,
                                     link=R.links.BASE_URL + R.links.ENDPOINT_CONTACTS,
                                     description="КОНТАКТЫ",
                                     browser=browser)
    write_to = ClickableComponent(locator=Locators.header.body_menu.WRITE_TO,
                                 link="",
                                 description="ЗАПИСАТЬСЯ",
                                 browser=browser)

    header.fast_link_menu = {
        items.ABOUT: about,
        items.MEDIA: media,
        items.OTZYVY: otzyvy,
        items.WORKPLACE: workplace,
        items.DEN_KLIENTA: den_klienta,
        items.TOUR_3D: tour_3d}
