from selenium.webdriver.common.by import By

from resources.resources import Resources


class _HeaderLocators:
    HEADER_COMMON = (By.XPATH, '//header[@class="bx-header"]')

class _MainPageLocators:
    BODY_TABS_USLUGI = (By.XPATH, '//a[text()="УСЛУГИ"]')
    HEADER_PHONE_NUMBER = (By.XPATH, f'//span[text()="{Resources.strings.PHONE_NUMBER}"]')


class Locators:
    main_page = _MainPageLocators()
    header = _HeaderLocators()
