from selenium.webdriver.common.by import By


class _BodyMenuLocators:
    MAIN = (By.XPATH, '//ul[@class="mmenuu"]//a[text()="ГЛАВНАЯ"]')
    USLUGI = (By.XPATH, '//ul[@class="mmenuu"]//a[text()="УСЛУГИ"]')
    MASTERS = (By.XPATH, '//ul[@class="mmenuu"]//a[text()="МАСТЕРА"]')
    PORTFOLIO = (By.XPATH, '//ul[@class="mmenuu"]//a[text()="НАШИ РАБОТЫ"]')
    CONTACTS = (By.XPATH, '//ul[@class="mmenuu"]//a[text()="КОНТАКТЫ"]')
    WRITE_TO = (By.XPATH, '//ul[@class="mmenuu"]//button[text()="ЗАПИСАТЬСЯ"]')
