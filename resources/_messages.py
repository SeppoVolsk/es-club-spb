from resources._colors import _Colors


class _ErrorsMessages():
    _err_color = _Colors.ORANGE_BG
    NOT_PRESENTED = f"{_err_color}нет такого элемента!{_Colors.RESET}"
    NOT_VISIBLE = f"{_err_color}не виден на странице!{_Colors.RESET}"
    NO_BROWSER = f"{_err_color}--browser_name should be chrome or firefox{_Colors.RESET}"
    INCORRECT_URL = f"{_err_color}Incorrect url:{_Colors.RESET}"


class _InfoMessages():
    _info_color = _Colors.CYAN
    START_CHROME = f"{_info_color}start Chrome browser for test..{_Colors.RESET}"
    START_FIREFOX = f"{_info_color}start Firefox browser for test..{_Colors.RESET}"
    QUIT_BROWSER = f"{_info_color}quit browser..{_Colors.RESET}"


class _HelpMessages():
    _help_color = _Colors.GREEN
    CHOOSE_BROWSER = f"{_help_color}Choose browser: chrome or firefox{_Colors.RESET}"
    CHOOSE_LANGUAGE = f"{_help_color}Choose user language{_Colors.RESET}"


class _Messages():
    error = _ErrorsMessages()
    info = _InfoMessages()
    help = _HelpMessages()
