from resources.resources import Resources


def test_body_menu_is_visible(header):
    assert header.body_menu.is_visible(), Resources.messages.error.BODY_MENU_NOT_VISIBLE
