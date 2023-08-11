from resources.resources import Resources


def test_header_is_visible(header, main_page):
    main_page.open()
    assert header.is_visible(), Resources.messages.ERROR_HEADER_NOT_VISIBLE


