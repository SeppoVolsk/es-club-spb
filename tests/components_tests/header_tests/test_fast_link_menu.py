from resources.resources import Resources


def test_fast_link_menu_is_visible(header):
    assert header.fast_link_menu.is_visible(), Resources.messages.error.HEADER_FAST_LINK_MENU_NOT_VISIBLE
