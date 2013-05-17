import asserts
from config import config
from page.www.main import Main
from unittest import TestCase
from testuser import User
from selenium.webdriver import Firefox

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

        expected_title = 'Web Hosting, Domain Names, eCommerce - Bluehost.com'
        title = page.selenium.title
        asserts.equal(title, expected_title)
        page = page.start_signup()

        expected_title = 'Sign Up Now - Web hosting provider - Bluehost.com'
        title = page.selenium.title
        asserts.equal(title, expected_title)
