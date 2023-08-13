from resources.resources import Resources


def test_phone_number_is_visible(header):
    assert header.phone_number_link.is_visible(), Resources.messages.error.HEADER_PHONE_NUMBER_NOT_VISIBLE
