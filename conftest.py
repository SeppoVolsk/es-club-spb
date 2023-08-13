import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
        print(f"\n{Resources.messages.info.START_CHROME}")
        browser = webdriver.Chrome(options=options)
    elif browser_name == Resources.strings.FIREFOX:
        print(f"\n{Resources.messages.info.START_FIREFOX}")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError(Resources.messages.error.NO_BROWSER)
    browser.implicitly_wait(Resources.values.IMPLICITLY_WAIT)
    yield browser
    print(f"\n{Resources.messages.info.QUIT_BROWSER}")
    browser.quit()

