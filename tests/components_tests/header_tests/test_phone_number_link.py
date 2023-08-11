from resources.resources import Resources


def test_phone_number_is_visible(header, main_page):
    main_page.open()
    assert header.phone_number_link.is_visible(), Resources.messages.ERROR_HEADER_PHONE_NUMBER_NOT_VISIBLE
