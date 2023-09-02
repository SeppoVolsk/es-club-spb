import pytest

from components.base_component import BaseComponent
from components.clickable_component import ClickableComponent
from locators.locators import Locators
from resources.resources import R


class Elements():
    search_input, search_button = range(2)


@pytest.fixture(autouse=True)
def define_search_row(main_page, browser):
    search_input = BaseComponent(locator=Locators.header.SEARCH_INPUT,
                                 description="Поле ввода",
                                 browser=browser)
    search_button = ClickableComponent(locator=Locators.header.SEARCH_BUTTON,
                                       link=R.links.BASE_URL + R.links.ENDPOINT_SEARCH_RESULT,
                                       description="Кнопка поиска (лупа)",
                                       browser=browser)
    main_page.header.search_row = [search_input, search_button]


@pytest.mark.si
def test_search_input_is_visible(main_page):
    assert (main_page
            .open()
            .header
            .search_row[Elements.search_input].is_visible()), R.strings.SEARCH_INPUT + R.messages.error.NOT_VISIBLE
