from resources.resources import R


def test_header_is_exists(header):
    assert header.is_exists(), R.messages.error.NOT_PRESENTED

def test_header_is_visible(header):
    assert header.is_exists(), R.strings.HEADER + R.messages.error.NOT_PRESENTED
    assert header.is_visible(), R.strings.HEADER + R.messages.error.NOT_VISIBLE



