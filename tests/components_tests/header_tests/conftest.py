import pytest

from components.clickable_component import ClickableComponent
from components.header.header import Header
from components.header.parts.address_schedule_block import AddressScheduleBlock
from components.header.parts.body_menu import BodyMenu
from components.header.parts.fast_link_menu import FastLinkMenu
from locators.locators import Locators
from resources.resources import Resources


@pytest.fixture()
def header(browser, open_main_page):
    return Header(browser=browser,

                  sale_link=ClickableComponent(locator=Locators.header.SALE_LINK_COMMON,
                                               link=Resources.links.BASE_URL + Resources.links.ENDPOINT_SALE,
                                               description="Ссылка Акции в красном квадрате",
                                               browser=browser),
                  phone_number_link=ClickableComponent(locator=Locators.header.PHONE_NUMBER,
                                                       link="tel:88124673030",
                                                       description='Надпись "+78124673030"',
                                                       browser=browser)
                  )
