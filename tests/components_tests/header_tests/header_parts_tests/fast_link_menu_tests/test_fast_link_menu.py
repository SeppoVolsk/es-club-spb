import pytest
from resources.resources import R


@pytest.mark.probe_flm
def test_fast_link_menu_is_visible(fast_link_menu):
    for menu_item in fast_link_menu.values():
        assert menu_item.is_visible(), menu_item.description + R.messages.error.NOT_VISIBLE



class TestFastLinkMenuItems():

    @pytest.mark.pro
    def test_fast_link_menu___about___link_is_correct(self, main_page, fast_link_menu, items):
        fast_link_menu[items.ABOUT].click()
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)

    def test_fast_link_menu___media___link_is_correct(self, main_page, fast_link_menu, items):
        fast_link_menu[items.MEDIA].click()
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_MEDIA
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)

    def test_fast_link_menu___workplace___link_is_correct(self, main_page, fast_link_menu, items):
        fast_link_menu[items.WORKPLACE].click()
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_WORKPLACE
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected, items)

    def test_fast_link_menu___den_klienta___link_is_correct(self, main_page, fast_link_menu, items):
        fast_link_menu[items.DEN_KLIENTA].click()
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_SALE_DEN_KLIENTA
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected, items)

    def test_fast_link_menu___otzyvy___link_is_correct(self, main_page, fast_link_menu, items):
        fast_link_menu[items.OTZYVY].click()
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_OTZYVY
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)

    def test_fast_link_menu___3d_tour___link_is_correct(self, main_page, fast_link_menu, items):
        fast_link_menu[items.TOUR_3D].click()
        current_url = main_page.current_url
        expected = R.links.BASE_URL + R.links.ENDPOINT_ABOUT_3D
        assert current_url == expected, R.messages.error.invalid_link(current_url, expected)
