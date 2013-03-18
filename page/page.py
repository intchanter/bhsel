import asserts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException


class Page():
    def __init__(self, setup):
        self.setup = setup
        self.base_url = setup.base_url
        self.selenium = setup.selenium
        self.timeout = setup.timeout

    def get_url(self, url):
        self.selenium.get(url)

    @property
    def is_the_current_page(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.selenium.title
        )
        asserts.contains(
            self.selenium.title,
            self._page_title,
            'Page title not found'
        )
        return True

    def get_current_url(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.selenium.title
        )

    def is_element_present(self, *locator):
        self.selenium.implicitly_wait(0)
        try:
            self.selenium.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            self.selenium.implicitly_wait(self.setup.default_implicit_wait)

    def is_element_visible(self, *locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except (NoSuchElementException, ElementNotVisibleException):
            return False

    def back(self):
        self.selenium.back()
