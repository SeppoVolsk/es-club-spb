import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page.main_page import MainPage
from resources.resources import Resources


@pytest.fixture()
def main_page(browser):
    main_page = MainPage(browser, Resources.links.BASE_URL)
    return main_page


@pytest.fixture()
def open_main_page(main_page):
    main_page.open()

