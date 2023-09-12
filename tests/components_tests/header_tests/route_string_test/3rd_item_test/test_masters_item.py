import pytest

from components.base_component import BaseComponent
from locators.locators import Locators
from resources.resources import R
from tests.components_tests.header_tests.body_menu_tests.conftest import define_body_menu
from tests.components_tests.header_tests.body_menu_tests.conftest import items_body_menu


class TestMastersItem:

    @pytest.fixture(autouse=True)
    def define_route_string_body_menu(self, main_page, items, browser):
        third_item = BaseComponent(locator=Locators.header.route_string.THIRD_ITEM,
                                   description="третий спан 'Мастера' в строке навигации",
                                   browser=browser)

        main_page.header.route_string[items.third.MASTERS] = third_item

    @pytest.mark.rs
    def test_masters_item_is_visible(self, main_page, items, items_body_menu):
        (main_page
         .open()
         .header
         .body_menu[items_body_menu.MASTERS]
         .click())
        assert (main_page
                .header
                .route_string[items.third.MASTERS]
                .is_visible()), (R.strings.ROUTE_STRING
                                 + main_page.header.route_string[items.third.MASTERS].description
                                 + R.messages.error.NOT_VISIBLE)

    def test_masters_item_url_is_correct(self, main_page, items, items_body_menu):
        (main_page
         .open()
         .header
         .body_menu[items_body_menu.MASTERS]
         .click())
        actual_link = main_page.current_url
        expected_link = R.links.BASE_URL + R.links.ENDPOINT_MASTERS
        assert actual_link == expected_link, R.messages.error.invalid_link(actual_link, expected_link)
