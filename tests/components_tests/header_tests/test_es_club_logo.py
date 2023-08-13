from resources.resources import Resources


def test_es_club_logo_is_visible(header):
    assert header.es_club_logo.is_visible(), Resources.messages.error.HEADER_ES_CLUB_LOGO_NOT_VISIBLE
