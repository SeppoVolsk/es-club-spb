import pytest

from components.base_component import BaseComponent
from locators.locators import Locators
from resources.resources import R


@pytest.fixture(autouse=True)
def address_schedule_block(main_page, browser):
    address_text = BaseComponent(browser=browser,
                                 locator=Locators.header.ADDRESS_COMMON,
                                 description="Надпись 'СПб, м.Приморская, Морская Набережная 29'")
    schedule_text = BaseComponent(browser=browser,
                                  locator=Locators.header.SCHEDULE_COMMON,
                                  description="Надпись 'ПН-СБ 10:00-21:00 ВС - выходной'")
    main_page.header.address_schedule_block = [address_text, schedule_text]


@pytest.mark.ads_probe
def test_address_schedule_block_is_visible(main_page):
    main_page.open()
    for every_text in main_page.header.address_schedule_block:
        assert every_text.is_visible(), R.strings.ADDRESS_SCHEDULE_BLOCK + R.messages.error.NOT_VISIBLE
