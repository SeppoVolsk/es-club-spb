import pytest
from resources.resources import R


@pytest.mark.pro
class TestFastMenuLinksAreCorrect():

    def test_fast_menu___about___link_is_correct(self, main_page, items):
        (main_page
         .open()
         .header
         .fast_menu[items.ABOUT]
         .click())
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)

    def test_fast_menu___media___link_is_correct(self, main_page, items):
        (main_page
         .open()
         .header
         .fast_menu[items.MEDIA]
         .click())
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_MEDIA
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)

    def test_fast_menu___workplace___link_is_correct(self, main_page, items):
        (main_page
         .open()
         .header
         .fast_menu[items.WORKPLACE]
         .click())
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_WORKPLACE
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected, items)

    def test_fast_menu___den_klienta___link_is_correct(self, main_page, items):
        (main_page
         .open()
         .header
         .fast_menu[items.DEN_KLIENTA]
         .click())
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_SALE_DEN_KLIENTA
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected, items)

    def test_fast_menu___otzyvy___link_is_correct(self, main_page, items):
        (main_page
         .open()
         .header
         .fast_menu[items.OTZYVY]
         .click())
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_OTZYVY
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)

    def test_fast_menu___3d_tour___link_is_correct(self, main_page, items):
        (main_page
         .open()
         .header
         .fast_menu[items.TOUR_3D]
         .click())
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_3D
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)
