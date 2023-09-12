from enum import *

import pytest

from tests.components_tests.header_tests.body_menu_tests.conftest import define_body_menu
from components.clickable_component import ClickableComponent
from locators.locators import Locators
from pages.main_page.main_page import MainPage
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
        GLAVNAYA = auto(),
        SALON = auto()

    class Item:
        first = _ItemsConst.GLAVNAYA
        second = _ItemsConst.SALON
        third = _ItemsThird.USLUGI

    return Item()


@pytest.fixture()
def setup_route_string_first_second_items(main_page, items, browser):
    first_item = ClickableComponent(locator=Locators.header.route_string.FIRST_ITEM,
                                    link=R.links.BASE_URL,
                                    description="первый спан 'Главная cтраница' в строке навигации",
                                    browser=browser)
    second_item = ClickableComponent(locator=Locators.header.fast_menu.MEDIA,
                                     link=R.links.BASE_URL + R.links.ENDPOINT_ABOUT,
                                     description="второй спан 'Салон красоты' в строке навигации",
                                     browser=browser)

    main_page.header.route_string = {
        items.first: first_item,
        items.second: second_item,
    }


@pytest.fixture()
def main_page(setup_route_string_first_second_items,
              define_body_menu,
              main_page) -> MainPage:
    return main_page
