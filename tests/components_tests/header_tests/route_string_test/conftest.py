from enum import *

import pytest

from components.clickable_component import ClickableComponent
from locators.locators import Locators
from resources.resources import R


@pytest.fixture(scope="session")
def items():
    class _ItemsUslugi(Enum):
        AFRO = auto(),
        OKRASHIVANIE = auto(),
        OMBRE = auto(),
        MRAMOR = auto(),
        STRIZHKA = auto(),
        UKLADKA = auto(),
        BIOZAVIVKA = auto(),
        BIOVYPRYAML = auto(),
        PRIKORNEVOY = auto(),
        ESTETICHESKOE = auto(),
        TERMO = auto(),
        KOMPLEKS = auto(),
        POLIROVKA = auto(),
        RECONSTRUKCIYA = auto(),
        ARHITEKTURA = auto(),
        BROVI = auto(),
        SOLYARIY = auto(),
        CRYOTOUCH = auto(),
        SOMATI = auto(),
        MAKIYAZH = auto()

    class _ItemsMasters(Enum):
        SEDOVA = auto(),
        KUZNETSOVA = auto(),
        AKIMKINA = auto()

    class _ItemsThird(Enum):
        USLUGI = auto(),
        MASTERS = auto(),
        PORTFOLIO = auto(),
        CONTACTS = auto()

    class _ItemsConst(Enum):
        GLAVNAYA=auto(),
        SALON=auto()
    class Item:
        FIRST = _ItemsConst.GLAVNAYA
        SECOND = _ItemsConst.SALON
        THIRD: _ItemsThird

    return Item()


@pytest.fixture()
def define_route_string(main_page, items, browser):
    about = ClickableComponent(locator=Locators.header.fast_menu.ABOUT,
                               link=R.links.BASE_URL + R.links.ENDPOINT_ABOUT,
                               description="О нас",
                               browser=browser)
    media = ClickableComponent(locator=Locators.header.fast_menu.MEDIA,
                               link=R.links.BASE_URL + R.links.ENDPOINT_ABOUT_MEDIA,
                               description="Медиа",
                               browser=browser)
    otzyvy = ClickableComponent(locator=Locators.header.fast_menu.OTZYVY,
                                link=R.links.BASE_URL + R.links.ENDPOINT_ABOUT_OTZYVY,
                                description="Отзывы",
                                browser=browser)
    workplace = ClickableComponent(locator=Locators.header.fast_menu.WORKPLACE,
                                   link=R.links.BASE_URL + R.links.ENDPOINT_ABOUT_WORKPLACE,
                                   description="Аренда",
                                   browser=browser)
    den_klienta = ClickableComponent(locator=Locators.header.fast_menu.SALE_DEN_KLIENTA,
                                     link=R.links.BASE_URL + R.links.ENDPOINT_ABOUT_SALE_DEN_KLIENTA,
                                     description="День клиента",
                                     browser=browser)
    tour_3d = ClickableComponent(locator=Locators.header.fast_menu.TOUR_3D,
                                 link=R.links.BASE_URL + R.links.ENDPOINT_ABOUT_3D,
                                 description="3d тур",
                                 browser=browser)

    main_page.header.fast_menu = {
        items.ABOUT: about,
        items.MEDIA: media,
        items.OTZYVY: otzyvy,
        items.WORKPLACE: workplace,
        items.DEN_KLIENTA: den_klienta,
        items.TOUR_3D: tour_3d}


@pytest.fixture()
def main_page(define_fast_menu, main_page):
    return main_page
