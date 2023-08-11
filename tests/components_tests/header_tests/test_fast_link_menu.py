from resources.resources import Resources


def test_fast_link_menu_is_visible(header, main_page):
    main_page.open()
    assert header.fast_link_menu.is_visible(), Resources.messages.ERROR_HEADER_FAST_LINK_MENU_NOT_VISIBLE
