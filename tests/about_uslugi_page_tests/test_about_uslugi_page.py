from resources.resources import Resources


def test_check_correct_url(about_uslugi_page):
    current_url = (about_uslugi_page
                   .open()
                   .should_be_about_uslugi_url())
    assert Resources.links.ENDPOINT_USLUGI in current_url, (
        f"{Resources.messages.ERROR_INCORRECT_URL}"
        f"Expected: {Resources.links.BASE_URL + Resources.links.ENDPOINT_USLUGI}"
        f"Actual: {current_url}"
    )
