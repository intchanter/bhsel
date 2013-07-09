from page.www.main import Main
import config
import asserts

def basic_signup(
        domain = config.config.existing_domain,
        domain_type = 'existing'
    ):
    '''
    Run through a full signup, using the specified domain name if provided.

    If domain_type is specified, pass it to the underlying code.

    Returns nothing.
    '''
    page = Main(config.config)
    page.selenium.get('http://www.bluehost.com')
    page.validate()  # Main page
    page = page.start_signup()
    page = page.choose_domain(domain, domain_type)
    page = page.submit_signup_form()
    page = page.complete_signup()
    page = page.go_cpm()
    page.wait_for_signup()
    page.verify_account()
    asserts.ok(page.flag_active('v'), 'Account is verified.')
