'''
Page objects for the signup process
'''

#import asserts
from page.page import Page
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import ElementNotVisibleException

elements = {
    'bluehost': {
        'expected_title': 'Sign Up Now - Web hosting provider - Bluehost.com',
        'wait_element': ('css', '#copyright'),
    },
    'fastdomain': {
    },
    'hostmonster': {
    },
    'justhost': {
    },
}

class Signup(Page):
    '''
    The first page of the signup process
    '''

    def __init__(self, config):
        super(Signup, self).__init__(config)
        self.expected_title = elements[self.config.brand]['expected_title']
