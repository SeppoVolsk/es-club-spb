import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from logger.logger import l
from resources.resources import Resources


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=Resources.strings.CHROME,
                     help=Resources.messages.help.CHOOSE_BROWSER)
    parser.addoption('--user_language', action='store', default=None,
                     help=Resources.messages.help.CHOOSE_LANGUAGE)


@pytest.fixture(scope="session")
def browser(request):
    options = Options()
    user_language = request.config.getoption("user_language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == Resources.strings.CHROME:
        l.info(f"\n{Resources.messages.info.START_CHROME}")
        browser = webdriver.Chrome(options=options)
    elif browser_name == Resources.strings.FIREFOX:
        l.info(f"\n{Resources.messages.info.START_FIREFOX}")
        browser = webdriver.Firefox()
    else:
        err_msg = Resources.messages.error.NO_BROWSER
        l.error(err_msg)
        raise pytest.UsageError(err_msg)
    browser.implicitly_wait(Resources.values.IMPLICITLY_WAIT)
    yield browser
    l.info(f"\n{Resources.messages.info.QUIT_BROWSER}")
    browser.quit()

