from selenium.webdriver.common.by import By

from locators.header.parts._fast_link_menu_locators import _FastLinkMenuLocators
from resources.resources import Resources


class _HeaderLocators:
    fast_link_menu = _FastLinkMenuLocators()
    HEADER_COMMON = (By.XPATH, '//header[@class="bx-header"]')
    FAST_LINK_MENU_COMMON = (By.XPATH, '//div[@class="fastlink"]')
    BODY_MENU_COMMON = (By.XPATH, '//div[@class="row"]')
    ES_CLUB_LOGO_COMMON = (By.XPATH, '//div[@class="logotop"]//img')
    SALE_LINK_COMMON = (By.XPATH, '//a[text()="Акции"]')
    BEAUTY_SALON_COMMON = (By.XPATH, '//a[text()="Салон красоты"]')
    ADDRESS_COMMON = (By.XPATH, '//div[@class="clock"]')
    SCHEDULE_COMMON = (By.XPATH, '//div[@class="place"]')
    ADDRES_MARK_COMMON = (By.XPATH, '//img[@src="/upload/medialibrary/edf/adres.png"]')
    PHONE_NUMBER = (By.XPATH, f'//span[text()="{Resources.strings.PHONE_NUMBER}"]')

