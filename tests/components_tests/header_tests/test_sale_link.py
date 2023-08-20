import pytest

from components.clickable_component import ClickableComponent
from locators.locators import Locators

from resources.resources import R


@pytest.fixture()
def define_sale_link(browser, main_page):
    (main_page
     .header) \
        .sale_link = ClickableComponent(locator=Locators.header.SALE_LINK_COMMON,
                                        link=R.links.BASE_URL + R.links.ENDPOINT_SALE,
                                        description="Ссылка Акции в красном квадрате",
                                        browser=browser)


class TestSaleLink:

    @pytest.fixture(autouse=True)
    def request_main_page(self, define_sale_link, main_page):
        self.main_page = main_page

    @pytest.mark.probe_sale_link
    def test_sale_link_is_visible(self):
        assert (self.main_page
                .open()
                .header
                .sale_link.is_visible()), R.strings.SALE_LINK + R.messages.error.NOT_VISIBLE

    def test_click_sale_link(self, main_page):
        (main_page
         .open()
         .header
         .sale_link
         .click())
        actual = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_SALE
        assert actual == expected, R.messages.error.invalid_link(actual, expected)
