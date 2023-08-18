import pytest
from components.clickable_component import ClickableComponent
from locators.locators import Locators
from resources.resources import R


@pytest.fixture()
def beauty_salon_link(header, browser):
    header.beauty_salon_link = ClickableComponent(locator=Locators.header.BEAUTY_SALON_COMMON,
                                                  link=R.links.BASE_URL,
                                                  description='Надпись "Салон Красоты"',
                                                  browser=browser)
    return header.beauty_salon_link


def test_beauty_salon_link_is_visible(beauty_salon_link):
    assert beauty_salon_link.is_visible(), R.strings.SALE_LINK + R.messages.error.NOT_VISIBLE


def test_click_beauty_salon_link(beauty_salon_link, current_url):
    beauty_salon_link.click()
    actual = current_url
    expected = R.links.BASE_URL
    assert actual == expected, R.messages.error.invalid_link(actual, expected)
