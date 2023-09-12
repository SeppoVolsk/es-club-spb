import pytest

from components.base_component import BaseComponent
from locators.locators import Locators
from resources.resources import R
from tests.components_tests.header_tests.body_menu_tests.conftest import define_body_menu
from tests.components_tests.header_tests.body_menu_tests.conftest import items_body_menu


class TestContactsItem:

    @pytest.fixture(autouse=True)
    def define_route_string_body_menu(self, main_page, items, browser):
        third_item = BaseComponent(locator=Locators.header.route_string.THIRD_ITEM,
                                   description="третий спан 'Контакты' в строке навигации",
                                   browser=browser)

        main_page.header.route_string[items.third.CONTACTS] = third_item

    @pytest.mark.rs
    def test_contacts_item_is_visible(self, main_page, items, items_body_menu):
        (main_page
         .open()
         .header
         .body_menu[items_body_menu.CONTACTS]
         .click())
        assert (main_page
                .header
                .route_string[items.third.CONTACTS]
                .is_visible()), (R.strings.ROUTE_STRING
                                 + main_page.header.route_string[items.third.CONTACTS].description
                                 + R.messages.error.NOT_VISIBLE)

    def test_contacts_item_url_is_correct(self, main_page, items, items_body_menu):
        (main_page
         .open()
         .header
         .body_menu[items_body_menu.CONTACTS]
         .click())
        actual_link = main_page.current_url
        expected_link = R.links.BASE_URL + R.links.ENDPOINT_CONTACTS
        assert actual_link == expected_link, R.messages.error.invalid_link(actual_link, expected_link)
