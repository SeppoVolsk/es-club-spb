import pytest

from components.base_component import BaseComponent
from locators.locators import Locators
from resources.resources import R
from tests.components_tests.header_tests.body_menu_tests.conftest import define_body_menu
from tests.components_tests.header_tests.body_menu_tests.conftest import items_body_menu


class Test1stItem:

    @pytest.mark.rs
    def test_1st_item_is_visible(self, main_page, items, items_body_menu):
        (main_page
         .open()
         .header
         .body_menu[items_body_menu.USLUGI]
         .click())
        assert (main_page
                .header
                .route_string[items.first]
                .is_visible()), (R.strings.ROUTE_STRING
                                 + main_page.header.route_string[items.first].description
                                 + R.messages.error.NOT_VISIBLE)

    def test_1st_item_url_is_correct(self, main_page, items, items_body_menu):
        (main_page
         .open()
         .header
         .body_menu[items_body_menu.USLUGI]
         .click())
        (main_page
         .header
         .route_string[items.first]
         .click())
        actual_link = main_page.current_url
        expected_link = R.links.BASE_URL
        assert actual_link == expected_link, R.messages.error.invalid_link(actual_link, expected_link)
