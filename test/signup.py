'''
Signup tests.
'''

import asserts
from config import config
from page.www.main import Main
from unittest import TestCase
from testuser import User
from utility import basic_signup


class TestSignup(TestCase):  # pylint: disable=R0904
    '''
    Test whether signup basically works.
    '''

    def setUp(self):
        self.user = User(config.selenium)
        self.user.login()

    def test_basic_signup(self):
        '''
        Run through a basic signup with no add-ons.
        '''
        basic_signup()  # contains the needed assertions

    # FIXME: The selenium object doesn't work on the second test.
    #def test_signup_with_domain(self):
        #'''
        #Run through a signup with a purchased domain.
        #'''
        #basic_signup(domain = config.new_domain, domain_type = 'existing')

    def tearDown(self):
        self.user.selenium.quit()
