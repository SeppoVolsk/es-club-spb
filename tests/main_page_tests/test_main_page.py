import pytest


from resources.resources import Resources, R


@pytest.mark.main_page
def test_current_url_is_base_url(main_page):
    assert (main_page
            .open()
            .current_url == R.links.BASE_URL), R.messages.error.INCORRECT_URL

