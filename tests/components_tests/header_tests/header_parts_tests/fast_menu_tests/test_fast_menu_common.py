import pytest

from resources.resources import R


@pytest.mark.probe_flm
def test_fast_menu_items_are_visible(main_page):
    (main_page
     .open())
    fast_menu_items = main_page.header.fast_menu.values()
    for menu_item in fast_menu_items:
        assert menu_item.is_visible(), menu_item.description + R.messages.error.NOT_VISIBLE
