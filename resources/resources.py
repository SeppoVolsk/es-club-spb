class _Messages():
    ERROR_HEADER_NOT_VISIBLE = "Header не отображается!"
    ERROR_NO_PHONE = "Phone number is not presented!"
    ERROR_NO_BROWSER = "--browser_name should be chrome or firefox"
    ERROR_INCORRECT_URL = "Incorrect url:"
    INFO_START_CHROME = "start Chrome browser for test.."
    INFO_START_FIREFOX = "start Firefox browser for test.."
    INFO_QUIT_BROWSER = "quit browser.."
    HELP_CHOOSE_BROWSER = "Choose browser: chrome or firefox"
    HELP_CHOOSE_LANGUAGE = "Choose user language"

class _Links():
    BASE_URL = "https://es-club.spb.ru/"
    ENDPOINT_USLUGI = "about/uslugi/"

class _Strings():
    CHROME = "chrome"
    FIREFOX = "firefox"
    PHONE_NUMBER = "+7 (812) 467-30-30"

class _Values():
    IMPLICITLY_WAIT = 30


class Resources():
    messages = _Messages()
    links = _Links()
    strings = _Strings()
    values = _Values()
