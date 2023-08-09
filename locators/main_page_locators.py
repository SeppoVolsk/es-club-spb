from selenium.webdriver.common.by import By


class MainPageLocators:
    BODY_TABS_USLUGI = (By.XPATH, '//a[text()="УСЛУГИ"]')
    HEADER_PHONE_NUMBER = (By.XPATH, '//span[text()="+7 (812) 467-30-30"]')