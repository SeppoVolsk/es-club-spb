from components.base_component import BaseComponent
from locators.locators import Locators


class AddressScheduleBlock(BaseComponent):
    address_block = BaseComponent()
    schedule_block = BaseComponent()
    def is_visible(self):
        return (super().is_visible(Locators.header.ADDRESS_COMMON)
                and super().is_visible(Locators.header.ADDRES_MARK_COMMON)
                and super().is_visible(Locators.header.SCHEDULE_COMMON))
