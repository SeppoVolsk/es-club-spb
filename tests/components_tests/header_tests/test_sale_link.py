import pytest

from components.clickable_component import ClickableComponent
from locators.locators import Locators
from resources.resources import R


@pytest.fixture()
def sale_link(browser, header):
    header.sale_link = ClickableComponent(locator=Locators.header.SALE_LINK_COMMON,
                                          link=R.links.BASE_URL + R.links.ENDPOINT_SALE,
                                          description="Ссылка Акции в красном квадрате",
                                          browser=browser)
    return header.sale_link


def test_sale_link_is_visible(header):
    assert header.sale_link.is_visible(), R.strings.SALE_LINK + R.messages.error.NOT_VISIBLE


@pytest.mark.probe_sale_link
def test_click_sale_link(sale_link, main_page):
    sale_link.click()
    actual = main_page.current_url
    expected = R.links.BASE_URL + R.links.ENDPOINT_SALE
    assert actual == expected, R.messages.error.invalid_link(actual, expected)
