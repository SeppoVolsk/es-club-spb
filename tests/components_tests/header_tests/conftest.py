import pytest
from components.header.header import Header



@pytest.fixture()
def header(browser):
    header = Header(browser)
    return header
