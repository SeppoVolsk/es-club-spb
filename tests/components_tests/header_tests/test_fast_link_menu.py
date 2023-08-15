import pytest

from components.header.parts.fast_link_menu import FastLinkMenu
from resources.resources import Resources
@pytest.fixture()
def fast_link_menu(header):
    fast_link_menu = header.fast_link_menu
    return fast_link_menu


def test_fast_link_menu_is_visible(fast_link_menu):
    assert fast_link_menu.is_visible(), Resources.messages.error.HEADER_FAST_LINK_MENU_NOT_VISIBLE

class TestFastLinkMenuItems():
    def test_fast_link_menu_about_item_link_is_correct(self, header, fast_link_menu):
        fast_link_menu.about_item.click()
        actual = header.current_url
        expected = Resources.links.BASE_URL + Resources.links.ENDPOINT_ABOUT
        assert actual == expected, f"Invalid link! Actual {actual} Expected {expected}"

    def test_fast_link_menu_about_media_item_link_is_correct(self, header, fast_link_menu):
        fast_link_menu.about_media_item.click()
        actual = header.current_url
        expected = Resources.links.BASE_URL + Resources.links.ENDPOINT_ABOUT_MEDIA
        assert actual == expected, f"Invalid link! Actual {actual} Expected {expected}"

    def test_fast_link_menu_about_workplace_item_link_is_correct(self, header, fast_link_menu):
        fast_link_menu.about_workplace_item.click()
        actual = header.current_url
        expected = Resources.links.BASE_URL + Resources.links.ENDPOINT_ABOUT_WORKPLACE
        assert actual == expected, f"Invalid link! Actual {actual} Expected {expected}"

    def test_fast_link_menu_about_sale_den_klienta_item_link_is_correct(self, header, fast_link_menu):
        fast_link_menu.about_sale_den_klienta_item.click()
        actual = header.current_url
        expected = Resources.links.BASE_URL + Resources.links.ENDPOINT_ABOUT_SALE_DEN_KLIENTA
        assert actual == expected, f"Invalid link! Actual {actual} Expected {expected}"

    def test_fast_link_menu_about_otzyvy_item_link_is_correct(self, header, fast_link_menu):
        fast_link_menu.about_otzyvy_item.click()
        actual = header.current_url
        expected = Resources.links.BASE_URL + Resources.links.ENDPOINT_ABOUT_OTZYVY
        assert actual == expected, f"Invalid link! Actual {actual} Expected {expected}"
    def test_fast_link_menu_about_3d_item_link_is_correct(self, header, fast_link_menu):
        fast_link_menu.about_3d_item.click()
        actual = header.current_url
        expected = Resources.links.BASE_URL + Resources.links.ENDPOINT_ABOUT_3D
        assert actual == expected, f"Invalid link! Actual {actual} Expected {expected}"