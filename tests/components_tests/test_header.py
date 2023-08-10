from resources.resources import Resources


def test_header_is_visible(header):
    assert (header
            .open()
            .isVisible()), Resources.messages.ERROR_HEADER_NOT_VISIBLE


def test_fastlink_urls(header):
    for e in (header
              .open()
              .fastlink
              .check_fastlink_items_urls()):
        print(e)
