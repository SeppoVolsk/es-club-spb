from pages.base_page import BasePage
from resources.resources import Resources


class AboutUslugiPage(BasePage):
    def should_be_about_uslugi_url(self):
        return self.browser.current_url
