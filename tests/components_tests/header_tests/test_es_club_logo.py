import pytest

from components.clickable_component import ClickableComponent
from locators.locators import Locators
from resources.resources import R


class TestEsClubLogo:

    @pytest.fixture(autouse=True)
    def _es_club_logo(self, header, browser):
        self.es_club_logo \
            = header.es_club_logo \
            = ClickableComponent(locator=Locators.header.ES_CLUB_LOGO_COMMON,
                                 link=R.links.BASE_URL,
                                 description="Логотип ES Club",
                                 browser=browser)

    def test_es_club_logo_is_visible(self):
        assert self.es_club_logo.is_visible(), R.strings.ES_CLUB_LOGO + R.messages.error.NOT_VISIBLE

    def test_es_club_logo_link_is_correct(self, main_page):
        self.es_club_logo.click()
        actual = main_page.current_url
        expected = R.links.BASE_URL
        assert actual == expected, R.messages.error.invalid_link(actual, expected)
