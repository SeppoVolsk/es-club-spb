from resources.resources import Resources


def test_header_is_visible(header):
    assert header.is_visible(), Resources.messages.error.HEADER_NOT_VISIBLE


