import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page.main_page import MainPage
from resources.resources import Resources


@pytest.fixture()
def main_page(browser) -> MainPage:
    main_page = MainPage(browser)
    return main_page


