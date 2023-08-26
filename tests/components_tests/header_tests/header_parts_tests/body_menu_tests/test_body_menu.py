import pytest

from resources.resources import R


class TestBodyMenuItems():

    @pytest.fixture(autouse=True)
    def main_page(self, define_body_menu, main_page):
        return main_page

    @pytest.mark.bodyprobe
    def test_body_menu___main___link_is_correct(self, main_page, items):
        (main_page
         .open()
         .header
         .body_menu[items.MAIN]
         .click())
        current_url = main_page.current_url
        expected_url = R.links.BASE_URL
        assert current_url == expected_url, R.messages.error.invalid_link(current_url, expected_url)

    @pytest.mark.bodyprobe
    def test_body_menu___uslugi___link_is_correct(self, main_page, items):
        (main_page
         .open()
         .header
         .body_menu[items.USLUGI]
         .click())
        current_url = main_page.current_url
        expected_url = R.links.BASE_URL + R.links.ENDPOINT_USLUGI
        assert current_url == expected_url, R.messages.error.invalid_link(current_url, expected_url)

    @pytest.mark.bodyprobe
    def test_body_menu___masters___link_is_correct(self, main_page, items):
        (main_page
         .open()
         .header
         .body_menu[items.MASTERS]
         .click())
        current_url = main_page.current_url
        expected_url = R.links.BASE_URL + R.links.ENDPOINT_MASTERS
        assert current_url == expected_url, R.messages.error.invalid_link(current_url, expected_url)

    @pytest.mark.bodyprobe
    def test_body_menu___contacts___link_is_correct(self, main_page, items):
        (main_page
         .open()
         .header
         .body_menu[items.CONTACTS]
         .click())
        current_url = main_page.current_url
        expected_url = R.links.BASE_URL + R.links.ENDPOINT_CONTACTS
        assert current_url == expected_url, R.messages.error.invalid_link(current_url, expected_url)

    @pytest.mark.bodyprobe
    def test_body_menu___portfolio___link_is_correct(self, main_page, items):
        (main_page
         .open()
         .header
         .body_menu[items.PORTFOLIO]
         .click())
        current_url = main_page.current_url
        expected_url = R.links.BASE_URL + R.links.ENDPOINT_PORTFOLIO
        assert current_url == expected_url, R.messages.error.invalid_link(current_url, expected_url)
