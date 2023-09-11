from selenium.webdriver.common.by import By


class _RouteStringLocators:
    FIRST_ITEM = (By.XPATH, '//div[@id="navigation"]/div/div[1]//span')
    SECOND_ITEM = (By.XPATH, '//div[@id="navigation"]/div/div[2]//span')
    THIRD_ITEM = (By.XPATH, '//div[@id="navigation"]/div/div[3]//span')
    FOURTH_ITEM = (By.XPATH, '//div[@id="navigation"]/div/div[4]//span')
