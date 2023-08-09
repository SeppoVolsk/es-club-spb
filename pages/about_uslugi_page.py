from pages.base_page import BasePage
from resources.resources import Resources


class AboutUslugiPage(BasePage):
    def should_be_about_uslugi_url(self):
        current_url = self.browser.current_url
        assert Resources.links.ENDPOINT_USLUGI in current_url, (
            f"{Resources.messages.ERROR_INCORRECT_URL}"
            f"Expected: {Resources.links.BASE_URL + Resources.links.ENDPOINT_USLUGI}"
            f"Actual: {current_url}"
        )