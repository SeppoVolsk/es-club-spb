import pytest

from components.base_component import BaseComponent
from locators.locators import Locators
from resources.resources import R
from tests.components_tests.header_tests.body_menu_tests.conftest import define_body_menu
from tests.components_tests.header_tests.body_menu_tests.conftest import items_body_menu


@pytest.fixture(autouse=True)
def define_route_string_body_menu(main_page, items, define_body_menu, browser):
    third_item = BaseComponent(locator=Locators.header.route_string.THIRD_ITEM,
                               description="Услуги",
                               browser=browser)

    main_page.header.route_string[items.third.USLUGI] = third_item


@pytest.mark.rs
def test_route_string_uslugi_is_visible(main_page, items, items_body_menu):
    (main_page
     .open()
     .header
     .body_menu[items_body_menu.USLUGI]
     .click())
    assert (main_page
            .header
            .route_string[items.third.USLUGI]
            .is_visible()), (R.strings.ROUTE_STRING
                             + main_page.header.route_string[items.third.USLUGI].description
                             + R.messages.error.NOT_VISIBLE)
