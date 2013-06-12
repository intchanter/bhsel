'''
Signup tests.
'''

import asserts
from config import config
from page.www.main import Main
from unittest import TestCase
from testuser import User


class TestSignup(TestCase):  # pylint: disable=R0904
    '''
    Test whether signup basically works.
    '''

    def setUp(self):
        self.user = User(config.selenium)

    def test_signup(self):
        '''
        Run through a basic signup with no add-ons.
        '''
        self.user.login()
        page = Main(config)
        page.selenium.get('http://www.bluehost.com')
        page.validate()  # Main page
        page = page.start_signup()
        page = page.choose_domain(config.existing_domain)
        page = page.submit_signup_form()
        page = page.complete_signup()
        page = page.go_cpm()
        page.wait_for_signup()
        page.verify_account()
        asserts.ok(page.flag_active('v'), 'Account is verified.')
