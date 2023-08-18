from enum import Enum, auto

import pytest

from components.clickable_component import ClickableComponent
from locators.locators import Locators
from resources.resources import R


class Item:
    (ABOUT,
     MEDIA,
     OTZYVY,
     WORKPLACE,
     DEN_KLIENTA,
     TOUR_3D) = range(6)


@pytest.fixture()
def fast_link_menu(header, browser):
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
        Item.ABOUT: about,
        Item.MEDIA: media,
        Item.OTZYVY: otzyvy,
        Item.WORKPLACE: workplace,
        Item.DEN_KLIENTA: den_klienta,
        Item.TOUR_3D: tour_3d}
    return header.fast_link_menu


@pytest.mark.probe_flm
def test_fast_link_menu_is_visible(fast_link_menu):
    for menu_item in fast_link_menu.values():
        assert menu_item.is_visible(), menu_item.description + R.messages.error.NOT_VISIBLE


@pytest.mark.pro
class TestFastLinkMenuItems():


    def test_fast_link_menu___about___link_is_correct(self, main_page, fast_link_menu):
        fast_link_menu[Item.ABOUT].click()
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)

    def test_fast_link_menu___media___link_is_correct(self, main_page, fast_link_menu):
        fast_link_menu[Item.MEDIA].click()
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_MEDIA
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)

    def test_fast_link_menu___workplace___link_is_correct(self, main_page, fast_link_menu):
        fast_link_menu[Item.WORKPLACE].click()
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_WORKPLACE
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)

    def test_fast_link_menu___den_klienta___link_is_correct(self, main_page, fast_link_menu):
        fast_link_menu[Item.DEN_KLIENTA].click()
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_SALE_DEN_KLIENTA
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)

    def test_fast_link_menu___otzyvy___link_is_correct(self, main_page, fast_link_menu):
        fast_link_menu[Item.OTZYVY].click()
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_OTZYVY
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)

    def test_fast_link_menu___3d_tour___link_is_correct(self, main_page, fast_link_menu):
        fast_link_menu[Item.TOUR_3D].click()
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_3D
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)
