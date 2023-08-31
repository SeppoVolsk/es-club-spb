import pytest

from components.header.header import Header
from resources.resources import R


@pytest.mark.header
class TestHeaderCommon:

    @pytest.fixture(autouse=True)
    def define_header(self, main_page, browser):
        main_page.header = Header(browser=browser)

    def test_header_is_exists(self, main_page):
        assert (main_page
                .open()
                .header.is_exists()), R.messages.error.NOT_PRESENTED

    def test_header_is_visible(self, main_page):
        assert (main_page
                .open()
                .header.is_exists()), R.strings.HEADER + R.messages.error.NOT_PRESENTED

        assert (main_page
                .open()
                .header.is_visible()), R.strings.HEADER + R.messages.error.NOT_VISIBLE
