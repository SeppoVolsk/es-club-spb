import pytest

from components.base_component import BaseComponent
from locators.locators import Locators
from resources.resources import R


@pytest.fixture()
def address_schedule_block(header, browser):
    address_notation = BaseComponent(browser=browser,
                                     locator=Locators.header.ADDRESS_COMMON,
                                     description="Надпись 'СПб, м.Приморская, Морская Набережная 29'")
    schedule_notation = BaseComponent(browser=browser,
                                      locator=Locators.header.SCHEDULE_COMMON,
                                      description="Надпись 'ПН-СБ 10:00-21:00 ВС - выходной'")
    header.address_schedule_block = [address_notation, schedule_notation]
    return header.address_schedule_block


@pytest.mark.ads_probe
def test_address_schedule_block_is_visible(address_schedule_block):
    for every_notation in address_schedule_block:
        assert every_notation.is_visible(), R.strings.ADDRESS_SCHEDULE_BLOCK + R.messages.error.NOT_VISIBLE
