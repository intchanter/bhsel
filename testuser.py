import json
import memcache
import requests

memcache_server = '127.0.0.1:11211'
key = 'test_user_pass'
day_seconds = 60 * 60 * 24
api_url = 'https://roster.bluehost.com/cgi-bin/admin/selenium_test_user'


class User(object):
    def __init__(self, selenium, username=None):
        if username is None:
            username = 'seleniumcron'
        self.username = username
        self.selenium = selenium
        self.brand = 'bluehost'
        self.web_pass = self.get_passwords()['web_pass']

    def get_passwords(self):
        mc = memcache.Client([memcache_server])
        passwords = mc.get(key)
        if passwords is None:
            passwords = self.set_passwords()
            mc.set(key, passwords)
        return json.loads(passwords)

    def set_passwords(self):
        args = {
            'user': self.username,
            'method': 'reset_pass',
        }
        response = requests.get(api_url, params=args)
        response.raise_for_status()
        return response.text

    def login(self):
        protocol = 'https://'
        page = '/cgi/admin/memcache'
        for site in ('www.bluehost.com', 'i.bluehost.com', 'my.bluehost.com'):
            url = protocol + site + page
            self.selenium.get(url)
            self.login_single_page()

    def login_single_page(self):
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
