from resources.resources import Resources


def test_address_schedule_block_is_visible(header):
    assert header.address_schedule_block.is_visible(), Resources.messages.error.HEADER_ES_CLUB_LOGO_NOT_VISIBLE
