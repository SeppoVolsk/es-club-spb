import pytest

from components.header.parts.address_schedule_block import AddressScheduleBlock
from resources.resources import Resources

@pytest.fixture()
def address_schedule_block(header, browser):
    header.address_schedule_block = AddressScheduleBlock(browser)
    return header.address_schedule_block


def test_address_schedule_block_is_visible(address_schedule_block):
    assert address_schedule_block.is_visible(), Resources.messages.error.HEADER_ES_CLUB_LOGO_NOT_VISIBLE
