'''
Manage Bluehost internal user logins
'''

import json
import memcache
import requests

memcache_server = '127.0.0.1:11211'
key = 'test_user_pass'
day_seconds = 60 * 60 * 24
api_url = 'https://roster.bluehost.com/cgi-bin/admin/selenium_test_user'


class User(object):
    '''The user object that will log in.'''

    def __init__(self, selenium, username=None):
        if username is None:
            username = 'seleniumcron'
        self.username = username
        self.selenium = selenium
        self.brand = 'bluehost'
        self.web_pass = self.get_passwords()['web_pass']

    def get_passwords(self):
        '''
        Pull the passwords from memcache or set new ones
        '''
        mc = memcache.Client([memcache_server])
        passwords = mc.get(key)
        if passwords is None:
            passwords = self.set_passwords()
            mc.set(key, passwords)
        if not ('web_pass' in passwords and 'other_pass' in passwords):
            print('Missing passwords.  We got: ', passwords)
        return json.loads(passwords)

    def set_passwords(self):
        '''
        Ask for new passwords to be set
        '''
        args = {
            'user': self.username,
            'method': 'reset_pass',
        }
        response = requests.get(api_url, params=args)
        response.raise_for_status()
        return response.text

    def login(self):
        '''
        Log in to all three clusters
        '''
        protocol = 'https://'
        page = '/cgi/admin/memcache'
        for site in ('www.bluehost.com', 'i.bluehost.com', 'my.bluehost.com'):
            url = protocol + site + page
            self.selenium.get(url)
            self.login_single_page()

    def login_single_page(self):
        '''
        Log in at the current page
        '''
        find_by_css = self.selenium.find_element_by_css_selector
        user_field = find_by_css('.login_username input')
        pass_field = find_by_css('.login_password input')
        login_button = find_by_css('.login_submit input')
        user_field.send_keys(self.username)
        pass_field.send_keys(self.web_pass)
        login_button.click()


if __name__ == '__main__':
    from selenium import webdriver
    user = User(webdriver.Firefox())
    print(user)
    user.login()
