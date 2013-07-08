'''
Handle per-test configuration.
'''

from selenium.webdriver import Firefox
import time


class Config(object):
    '''
    Holds the configuration information for a given test run.
    '''
    def __init__(self, selenium, base_url, brand, timeout=5):
        self.selenium = selenium
        self.base_url = base_url
        self.timeout = timeout
        self.brand = brand
        self.debug = True
        timestamp = int(time.time())
        self.existing_domain = 'qa-sel-{}.ru'.format(timestamp)
        self.new_domain = 'qa-sel-{}.com'.format(timestamp)

config = Config(Firefox(), 'http://www.bluehost.com/', 'bluehost')
