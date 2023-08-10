import pytest
from components.header.header import Header
from resources.resources import Resources


@pytest.fixture()
def header(browser):
    header = Header(browser, Resources.links.BASE_URL)
    return header
