import pytest

from resources.resources import Resources


class TestEsClubLogo:

    @pytest.fixture(autouse=True)
    def _request_header(self, header):
        self.header = header

    def test_es_club_logo_is_visible(self):
        assert self.header.es_club_logo.is_visible(), Resources.messages.error.HEADER_ES_CLUB_LOGO_NOT_VISIBLE

    def test_es_club_logo_link_is_correct(self):
        self.header.es_club_logo.click()
        actual = self.header.current_url
        expected = Resources.links.BASE_URL
        assert actual == expected, f"Invalid link! Actual {actual} Expected {expected}"
