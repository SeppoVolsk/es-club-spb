import pytest

from components.clickable_component import ClickableComponent
from locators.locators import Locators
from resources.resources import R


@pytest.fixture()
def phone_number_link(browser, header):
    header.phone_number_link = ClickableComponent(locator=Locators.header.PHONE_NUMBER,
                                                  link="tel:88124673030",
                                                  description='Надпись "+78124673030"',
                                                  browser=browser)
    return header.phone_number_link


@pytest.mark.phone_probe
def test_phone_number_is_visible(phone_number_link):
    assert phone_number_link.is_visible(), R.strings.PHONE_NUMBER + R.messages.error.NOT_VISIBLE
