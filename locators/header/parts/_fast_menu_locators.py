from selenium.webdriver.common.by import By


class _FastMenuLocators:
    ABOUT = (By.XPATH, '//a[text()="О нас"]')
    MEDIA = (By.XPATH, '//a[text()="Медиа"]')
    OTZYVY = (By.XPATH, '//a[text()="Отзывы"]')
    WORKPLACE = (By.XPATH, '//a[text()="Аренда"]')
    SALE_DEN_KLIENTA = (By.XPATH, '//a[text()="Аренда"]//following::a')
    TOUR_3D = (By.XPATH, '//b[text()="3D-тур"]')
