'''
Page objects for the signup process
'''

#import asserts
from page.page import Page
from page.i.cpm import CPM
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import ElementNotVisibleException

elements = {
    'bluehost': {
        'existing_domain_field': (
            'css', 'form[name=transfer] input[name=domain]'),
        'existing_domain_next': (
            'css', 'form[name=transfer] input[type=submit]'),
        'expected_title': (
            'Sign Up Now - Web hosting provider - Bluehost.com'),
        'choose_domain_expected_title': (
            'Sign Up Now - Web hosting provider - Bluehost.com'),
        'signup_form_expected_title': (
            'Sign Up - Congratulations! - Web hosting provider - Bluehost.com'
        ),
        'addons_expected_title': (
            'Additional Options - Web hosting provider - Bluehost.com'),
        'congratulations_expected_title': (
            'Sign Up Complete - Web hosting provider - Bluehost.com'),
        'new_domain_field': ('css', 'form[name=register] input[name=domain]'),
        'new_domain_tld': ('css', 'form[name=register] select'),
        'new_domain_next': ('css', 'form[name=register] input[type=submit]'),
        'wait_element': ('css', '#copyright'),
        'autosubmit_link': ('css', 'li span:last-of-type a.auto_submit'),
        'complete_button': ('css', 'input#buy_now'),
        'cpm_link': ('link text', 'cPanel Manager'),
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
        self.elements = elements[self.config.brand]

    def choose_domain(self, domain, kind='existing'):
        '''
        Enter and submit the domain name using an existing domain.
        '''

        if kind == 'existing':
            field = self.selenium.find_element(
                *self.elements['existing_domain_field']
            )
            button = self.selenium.find_element(
                *self.elements['existing_domain_next']
            )
            field.send_keys(domain)
            button.click()
        elif kind == 'new':
            domain_field = self.selenium.find_element(
                *self.elements['new_domain_field']
            )
            button = self.selenium.find_element(
                *self.elements['new_domain_next']
            )
            tld_field = self.selenium.find_element(
                *self.elements['new_domain_tld']
            )
            domain, tld = domain.split('.', 1)
            domain_field.send_keys(domain)
            tld_field.send_keys(tld)
            button.click()
        else:
            raise ValueError(
                'Domain kind/type must be "existing" or "new", got: {}'
                .format(kind)
            )
        self.elements['expected_title'] = self.elements[
            'signup_form_expected_title'
        ]
        self.validate()
        return self

    def submit_signup_form(self):
        '''
        Use the autofill link to fill and submit the employee-specific
        signup data.
        '''

        autofill_link = self.selenium.find_element(
            *self.elements['autosubmit_link']
        )
        autofill_link.click()
        self.elements['expected_title'] = self.elements[
            'addons_expected_title'
        ]
        self.validate()
        return self

    def complete_signup(self):
        '''
        Press the button to complete the signup.
        '''

        button = self.selenium.find_element(*self.elements['complete_button'])
        button.click()
        self.elements['expected_title'] = self.elements[
            'congratulations_expected_title'
        ]
        self.validate()
        return self

    def go_cpm(self):
        '''
        Do something
        '''
        link = self.selenium.find_element(*self.elements['cpm_link'])
        link.click()
        return CPM(self.config)
