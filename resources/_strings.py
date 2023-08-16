from resources._colors import _Colors


class _Strings():
    _title_color = _Colors.PURPLE_BG
    CHROME = f"{_title_color}chrome{_Colors.RESET}"
    FIREFOX = f"{_title_color}firefox{_Colors.RESET}{_Colors.RESET}"
    PHONE_NUMBER = "+7 (812) 467-30-30"
    HEADER = f"{_title_color}Header{_Colors.RESET}"
    FAST_LINK_MENU = f"{_title_color}Header->FastLinkMenu{_Colors.RESET}"
    BODY_MENU = f"{_title_color}Header->BodyMenu{_Colors.RESET}"
    ES_CLUB_LOGO = f"{_title_color}Header->EsClubLogo{_Colors.RESET}"
    SALE_LINK = f"{_title_color}Header->SaleLink{_Colors.RESET}"
    BEAUTY_SALON_LINK = f"{_title_color}Header->BeautySalonLink{_Colors.RESET}"

print(_Strings.ES_CLUB_LOGO)