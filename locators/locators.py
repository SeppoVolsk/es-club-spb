from locators.body._body_locators import _BodyLocators
from locators.footer._footer_locators import _FooterLocators
from locators.header._header_locators import _HeaderLocators
from locators._main_page_locators import _MainPageLocators


class Locators:
    main_page = _MainPageLocators()
    header = _HeaderLocators()
    body = _BodyLocators()
    footer = _FooterLocators()
