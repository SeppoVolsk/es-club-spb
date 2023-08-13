from selenium.webdriver.common.by import By

from resources.resources import Resources


class _MainPageLocators:
    BODY_TABS_USLUGI = (By.XPATH, '//a[text()="УСЛУГИ"]')
    PHONE_NUMBER = (By.XPATH, f'//span[text()="{Resources.strings.PHONE_NUMBER}"]')