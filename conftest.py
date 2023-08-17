import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from logger.logger import l
from resources.resources import R


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=R.strings.CHROME,
                     help=R.messages.help.CHOOSE_BROWSER)
    parser.addoption('--user_language', action='store', default=None,
                     help=R.messages.help.CHOOSE_LANGUAGE)
    parser.addoption('--log_level', '--ll', action='store', default="info",
                     help=R.messages.help.CHOOSE_LOG_LEVEL)


@pytest.fixture(scope="session")
def log_level(request):
    log_level:str = request.config.getoption('--log_level', '--ll')
    match log_level.lower():
        case "debug": R.values.LOGGING_LEVEL = logging.DEBUG
        case "info": R.values.LOGGING_LEVEL = logging.INFO
        case "warning": R.values.LOGGING_LEVEL = logging.WARNING
        case "error": R.values.LOGGING_LEVEL = logging.ERROR


@pytest.fixture(scope="session")
def browser(request, log_level):
    options = Options()
    user_language = request.config.getoption("user_language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == R.strings.CHROME:
        l.info(f"{R.messages.info.START_CHROME}")
        browser = webdriver.Chrome(options=options)
    elif browser_name == R.strings.FIREFOX:
        l.info(f"{R.messages.info.START_FIREFOX}")
        browser = webdriver.Firefox()
    else:
        err_msg = R.messages.error.NO_BROWSER
        l.error(err_msg)
        raise pytest.UsageError(err_msg)
    browser.implicitly_wait(R.values.IMPLICITLY_WAIT)
    yield browser
    l.info(f"{R.messages.info.QUIT_BROWSER}")
    browser.quit()

