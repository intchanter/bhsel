'''
Create an interface around our pages.
'''

from page.page import Page
from page.www.signup import Signup
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import ElementNotVisibleException

class Main(Page):
    '''
    Page object for www.<brand>.<tld>/.
    '''
    def start_signup(self):
        '''
        Clicks the Signup button on the first page
        '''
        button = self.selenium.find_element_by_css_selector('img.signup_button')
        button.click()
        return Signup(self.config)
