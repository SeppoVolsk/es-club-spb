from resources.resources import Resources


def test_sale_link_is_visible(header):
    assert header.sale_link.is_visible(), Resources.messages.error.HEADER_SALE_LINK_NOT_VISIBLE

def test_click_sale_link(header):
    header.sale_link.click()
    actual = header.current_url
    expected = Resources.links.BASE_URL + Resources.links.ENDPOINT_SALE
    assert actual == expected, f"Invalid link! Actual {actual} Expected {expected}"
