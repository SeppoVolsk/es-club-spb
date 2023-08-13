from selenium.webdriver.common.by import By
from resources.resources import Resources


class _HeaderLocators:
    HEADER_COMMON = (By.XPATH, '//header[@class="bx-header"]')
    FAST_LINK_MENU_COMMON = (By.XPATH, '//div[@class="fastlink"]')
    BODY_MENU_COMMON = (By.XPATH, '//div[@class="row"]')
    ES_CLUB_LOGO_COMMON = (By.XPATH, '//div[@class="logotop"]//img')
    SALE_LINK_COMMON = (By.XPATH, '//div[@class="sale"]')
    BEAUTY_SALON_COMMON = (By.XPATH, '//a[text()="Салон красоты"]')
    ADDRESS_COMMON = (By.XPATH, '//div[@class="clock"]')
    SCHEDULE_COMMON = (By.XPATH, '//div[@class="place"]')
    ADDRES_MARK_COMMON = (By.XPATH, '//img[@src="/upload/medialibrary/edf/adres.png"]')
    PHONE_NUMBER = (By.XPATH, f'//span[text()="{Resources.strings.PHONE_NUMBER}"]')
