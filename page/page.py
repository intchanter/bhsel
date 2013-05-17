'''
Creates the page object interface
'''

import asserts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

class Page(object):
    '''
    Represents a single page.
    '''
    def __init__(self, config):
        self.config = config
        self.base_url = config.base_url
        self.selenium = config.selenium
        self.timeout = config.timeout
        self.expected_title = 'UNDEFINED TITLE'

    def get_url(self, url):
        '''
        Loads the specified URL.
        '''
        self.selenium.get(url)

    def is_the_current_page(self):
        '''
        Does this object represent the current page?  Return the answer.
        '''
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.selenium.title
        )
        return self.expected_title in self.selenium.title

    def validate(self):
        '''
        Ensure that we're on the page this object represents.
        '''
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.selenium.title
        )
        asserts.contains(self.selenium.title, self.expected_title)

    def get_current_url(self):
        '''
        Wait for a title to exist, then return the current URL.
        '''
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
            self.selenium.implicitly_wait(self.config.default_implicit_wait)

    def is_element_visible(self, *locator):
        '''
        Return a boolean indicating the visibility of the element
        '''
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except (NoSuchElementException, ElementNotVisibleException):
            return False

    def back(self):
        self.selenium.back()
