import asserts
from page.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

values = {
    'bluehost': {
        'expected_title': 'Sign Up Now - Web hosting provider - Bluehost.com',
    },
    'fastdomain': {
    },
    'hostmonster': {
    },
    'justhost': {
    },
}
class Signup(Page):
    def __init__(self, config):
        super().__init__(config)
        self.expected_title = values[self.config.brand]['expected_title']
