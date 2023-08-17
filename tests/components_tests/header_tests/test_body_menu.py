import pytest

from components.header.parts.body_menu import BodyMenu
from resources.resources import Resources


@pytest.fixture()
def body_menu(header, browser):
    header.body_menu = BodyMenu(browser)
    return header.body_menu

def test_body_menu_is_visible(body_menu):
    assert body_menu.is_visible(), Resources.messages.error.BODY_MENU_NOT_VISIBLE
