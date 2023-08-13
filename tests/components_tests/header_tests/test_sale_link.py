from resources.resources import Resources


def test_sale_link_is_visible(header):
    assert header.sale_link.is_visible(), Resources.messages.error.HEADER_SALE_LINK_NOT_VISIBLE
