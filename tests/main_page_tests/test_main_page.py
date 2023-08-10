from locators.locators import Locators
from resources.resources import Resources


def test_go_to_uslugi(main_page):
    (main_page
     .open()
     .go_to_uslugi_tab())


def test_phone_number_should_be_shown(main_page):
    actual = (main_page
              .open()
              .should_be_phone_number())
    assert actual == Resources.strings.PHONE_NUMBER, Resources.messages.ERROR_NO_PHONE + actual
