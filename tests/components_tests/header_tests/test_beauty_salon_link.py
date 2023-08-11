from resources.resources import Resources


def test_beauty_salon_link_is_visible(header, main_page):
    main_page.open()
    assert header.beauty_salon_link.is_visible(), Resources.messages.ERROR_HEADER_BEAUTY_SALON_LINK_NOT_VISIBLE
