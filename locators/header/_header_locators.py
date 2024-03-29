from selenium.webdriver.common.by import By

from locators.header.parts._body_menu_locators import _BodyMenuLocators
from locators.header.parts._fast_menu_locators import _FastMenuLocators
from locators.header.parts._route_string_locators import _RouteStringLocators
from resources.resources import Resources


class _HeaderLocators:
    fast_menu = _FastMenuLocators()
    body_menu = _BodyMenuLocators()
    route_string = _RouteStringLocators()
    HEADER_COMMON = (By.XPATH, '//header')
    FAST_LINK_MENU_COMMON = (By.XPATH, '//div[@class="fastlink"]')
    BODY_MENU_COMMON = (By.XPATH, '//div[@class="row"]')
    ES_CLUB_LOGO_COMMON = (By.XPATH, '//div[@class="logotop"]//img')
    SALE_LINK_COMMON = (By.XPATH, '//a[text()="Акции"]')
    BEAUTY_SALON_COMMON = (By.XPATH, '//a[text()="Салон красоты"]')
    ADDRESS_COMMON = (By.XPATH, '//div[@class="clock"]')
    SCHEDULE_COMMON = (By.XPATH, '//div[@class="place"]')
    ADDRES_MARK_COMMON = (By.XPATH, '//img[@src="/upload/medialibrary/edf/adres.png"]')
    PHONE_NUMBER = (By.XPATH, f'//span[text()="{Resources.strings.PHONE_NUMBER}"]')
    SEARCH_INPUT = (By.XPATH, '//input[@id="title-search-input"]')
    SEARCH_BUTTON = (By.XPATH, '//span[@class="bx-input-group-btn"]')

