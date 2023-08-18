import pytest

from components.header.header import Header


@pytest.fixture()
def header(browser, open_main_page):
    return Header(browser=browser)
