import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.about_uslugi_page.about_uslugi_page import AboutUslugiPage
from pages.main_page.main_page import MainPage
from resources.resources import Resources


@pytest.fixture()
def about_uslugi_page(browser):
    about_uslugi_page = AboutUslugiPage(browser,
                                        Resources.links.BASE_URL + Resources.links.ENDPOINT_USLUGI)
    return about_uslugi_page
