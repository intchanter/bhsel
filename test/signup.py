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

    def test_basic_signup(self):
        '''
        Run through a basic signup with no add-ons.
        '''
        self.user.login()
        basic_signup()  # contains the needed assertions

    def tearDown(self):
        self.user.selenium.quit()
