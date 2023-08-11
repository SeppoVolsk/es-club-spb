from resources.resources import Resources


def test_sale_link_is_visible(header, main_page):
    main_page.open()
    assert header.sale_link.is_visible(), Resources.messages.ERROR_HEADER_SALE_LINK_NOT_VISIBLE
