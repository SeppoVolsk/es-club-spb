from resources.resources import Resources


def test_address_schedule_block_is_visible(header, main_page):
    main_page.open()
    assert header.address_schedule_block.is_visible(), Resources.messages.ERROR_HEADER_ES_CLUB_LOGO_NOT_VISIBLE