from resources.resources import Resources


def test_body_menu_is_visible(header, main_page):
    main_page.open()
    assert header.body_menu.is_visible(), Resources.messages.ERROR_BODY_MENU_NOT_VISIBLE
