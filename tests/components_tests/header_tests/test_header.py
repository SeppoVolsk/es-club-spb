from resources.resources import R


def test_header_is_on_page(header):
    assert header.is_on_page(), R.messages.error.ELEMENT_NOT_PRESENTED

def test_header_is_visible(header):
    assert header.is_visible(), R.messages.error.HEADER_NOT_VISIBLE


