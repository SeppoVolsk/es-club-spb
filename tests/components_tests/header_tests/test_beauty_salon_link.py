import pytest
from components.clickable_component import ClickableComponent
from locators.locators import Locators
from resources.resources import R


@pytest.fixture(autouse=True)
def define_beauty_salon_link(main_page, browser):
    main_page.header.beauty_salon_link = ClickableComponent(locator=Locators.header.BEAUTY_SALON_COMMON,
                                                            link=R.links.BASE_URL,
                                                            description='Надпись "Салон Красоты"',
                                                            browser=browser)

def test_beauty_salon_link_is_visible(main_page):
    assert (main_page
            .open()
            .header
            .beauty_salon_link.is_visible()), R.strings.SALE_LINK + R.messages.error.NOT_VISIBLE


def test_click_beauty_salon_link(main_page):
    (main_page
     .open()
     .header
     .beauty_salon_link.click())
    actual = main_page.current_url
    expected = R.links.BASE_URL
    assert actual == expected, R.messages.error.invalid_link(actual, expected)
