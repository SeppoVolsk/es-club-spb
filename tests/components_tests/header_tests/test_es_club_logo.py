from resources.resources import Resources


def test_es_club_logo_is_visible(header, main_page):
    main_page.open()
    assert header.es_club_logo.is_visible(), Resources.messages.ERROR_HEADER_ES_CLUB_LOGO_NOT_VISIBLE