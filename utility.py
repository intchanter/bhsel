from page.www.main import Main
from config import config
import asserts

def basic_signup(domain = config.existing_domain):
    page = Main(config)
    page.selenium.get('http://www.bluehost.com')
    page.validate()  # Main page
    page = page.start_signup()
    page = page.choose_domain(domain)
    page = page.submit_signup_form()
    page = page.complete_signup()
    page = page.go_cpm()
    page.wait_for_signup()
    page.verify_account()
    asserts.ok(page.flag_active('v'), 'Account is verified.')
