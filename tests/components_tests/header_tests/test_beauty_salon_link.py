from resources.resources import Resources


def test_beauty_salon_link_is_visible(header):
    assert header.beauty_salon_link.is_visible(), Resources.messages.error.HEADER_BEAUTY_SALON_LINK_NOT_VISIBLE

def test_click_beauty_salon_link(header):
    header.beauty_salon_link.click()
    actual = header.current_url
    expected = Resources.links.BASE_URL
    assert actual == expected, f"Invalid link! Actual {actual} Expected {expected}"