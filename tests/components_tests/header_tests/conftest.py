import pytest

from components.header.header import Header


@pytest.fixture()
def header(main_page):
    return main_page.header
