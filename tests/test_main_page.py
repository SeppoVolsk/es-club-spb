from pages.main_page import MainPage
from resources.resources import Resources


def test_go_to_uslugi(browser):
    main_page = MainPage(browser, Resources.links.BASE_URL)
    main_page.open()
    main_page.go_to_uslugi_tab()

def test_phone_number_should_be_shown(browser):
    main_page = MainPage(browser, Resources.links.BASE_URL)
    main_page.open()
    main_page.should_be_phone_number()