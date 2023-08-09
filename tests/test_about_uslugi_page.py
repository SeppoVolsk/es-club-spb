from pages.about_uslugi_page import AboutUslugiPage
from resources.resources import Resources


def test_check_correct_url(browser):
    url = Resources.links.BASE_URL + Resources.links.ENDPOINT_USLUGI
    about_uslugi_page = AboutUslugiPage(browser, url)
    about_uslugi_page.open()
    about_uslugi_page.should_be_about_uslugi_url()
