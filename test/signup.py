import asserts
from config import config
from page.www.main import Main
from unittest import TestCase
from testuser import User

class TestSignup(TestCase):  # pylint: disable=R0904
    '''
    Test whether signup works.
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
        page.validate()
        page = page.start_signup()
        page.validate()
