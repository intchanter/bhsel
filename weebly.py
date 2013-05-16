#!/usr/bin/env python

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from testuser import User
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import os
import tarfile

def cpm_get_info():
    u = browser.find_element_by_class_name('subtitle').text
    (dom2, custid, user, box, address) = u.split(' | ')
    (ip, junk) = address.split( )
    (junk,dom) = dom2.split( )
    return (custid, user, box, ip, dom)

def wait_for_signup():
    while not (browser.find_elements_by_link_text('cPanel')):
        time.sleep(150)
        browser.refresh()
        input('press enter when cpanel is installed')
    return

def upgrade(type):
    browser.switch_to_default_content()
    browser.find_element_by_css_selector('div#header_upgrade img').click()
    WebDriverWait(browser, 10).until(lambda d : d.find_element_by_link_text('Select Domain')).click()
    if (type == 'pro'):
        WebDriverWait(browser, 10).until(lambda d : d.find_element_by_name('add_proaccount')).click()
    elif (type == 'ecom'):
        WebDriverWait(browser, 10).until(lambda d : d.find_element_by_name('add_ecommerce')).click()
    browser.find_element_by_css_selector('.btn_primary.add_to_cart').click()
    browser.find_element_by_name('CVV2_EXISTING').send_keys('349')
    browser.find_element_by_css_selector('button.btn_primary').click()
    browser.switch_to_alert().accept()
#users.login_single_page()
    time.sleep(90)
    if not(browser.find_elements_by_link_text('Click here')):
        users.login_single_page()
        browser.find_element_by_css_selector('button.btn_primary').click()
        browser.switch_to_alert().accept()
        time.sleep(60)
    WebDriverWait(browser, 10).until(lambda d : d.find_element_by_link_text('Click here')).click()
    WebDriverWait(browser, 10).until(lambda d : d.find_element_by_link_text('Hosting')).click()


def signup():
    browser.get('http://www.bluehost.com')
    browser.get_screenshot_as_file(path + '/signup1.png')
    browser.find_element_by_css_selector('img.signup_button').click()
    #WebDriverWait(browser, 10).until(lambda d : d.find_element_by_css_selector('img.signup_button')).click()
    WebDriverWait(browser, 10).until(lambda d : d.find_element_by_id('domain')).clear()
    browser.get_screenshot_as_file(path + '/signup2.png')
    browser.find_element_by_id('domain').send_keys(domain)
    browser.find_element_by_xpath('//input[@value="Next"]').click()
    browser.find_element_by_link_text('Employee Test Data "Approved"').click()
    browser.find_element_by_name('next').click()
    browser.get_screenshot_as_file(path + '/signup3.png')
    browser.find_element_by_id('buy_now').click()
    browser.get_screenshot_as_file(path + '/signup4.png')
    browser.find_element_by_link_text('cPanel Manager').click()
    browser.get_screenshot_as_file(path + '/cpm.png')


def non_pro_test():
    time.sleep(20)
    frame = browser.find_element_by_css_selector('iframe')
    browser.switch_to_frame(frame)
    chains = webdriver.ActionChains(browser)
    WebDriverWait(browser, 30).until(lambda d : d.find_element_by_name('id_58462494'))
    chains.drag_and_drop(browser.find_element_by_name('id_58462494'), browser.find_element_by_id('empty-message-inner')).perform()
    time.sleep(3)
    browser.find_element_by_id('logo').click()
    chains = webdriver.ActionChains(browser)
    time.sleep(3)
    chains.click_and_hold(browser.find_element_by_name('id_20731748'))
    time.sleep(3)
    chains.release(browser.find_element_by_class_name('weebly-content-area')).perform()
    #chains.drag_and_drop(browser.find_element_by_name('id_20731748'), browser.find_element_by_class_name('element-box-contents')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    time.sleep(3)
    chains.drag_and_drop(browser.find_element_by_name('id_87358824'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_62850560'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_44785763'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_51424376'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_92495494'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_45444132'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_59396708'), browser.find_element_by_class_name('weebly-content-area')).perform()
    browser.find_element_by_link_text('Multimedia').click()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_18362204'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_31574711'), browser.find_element_by_class_name('weebly-content-area')).perform()
    browser.find_element_by_link_text('Continue').click()
    browser.find_element_by_class_name('weebly-dialog-close').click()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_46196121'), browser.find_element_by_class_name('weebly-content-area')).perform()
    handles = browser.window_handles
    browser.switch_to_window(handles[2])
    browser.get_screenshot_as_file(path + '/upsell.png')
    browser.close()
    browser.switch_to_window(handles[1])
    frame = browser.find_element_by_css_selector('iframe')
    browser.switch_to_frame(frame)
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    time.sleep(3)
    chains.drag_and_drop(browser.find_element_by_name('id_64190838'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_42844424'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_85353141'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_8893461'), browser.find_element_by_class_name('weebly-content-area')).perform()
    browser.find_element_by_link_text('More').click()
    browser.find_element_by_link_text('Layout').click()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_79078446'), browser.find_element_by_class_name('weebly-content-area')).perform()
    browser.find_element_by_link_text('Misc').click()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_62317151'), browser.find_element_by_class_name('weebly-content-area')).perform()
    browser.find_element_by_link_text('Forms').click()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_20040879'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_42391650'), browser.find_element_by_class_name('weebly-content-area')).perform()
    browser.find_element_by_link_text('Design').click()
    browser.find_element_by_id('theme_417534755793912073').click()
    browser.find_element_by_id('theme_189529082218988161').click()
    browser.find_element_by_id('theme_753078197207386506').click()
    browser.find_element_by_id('theme_701731089317975641').click()
    browser.find_element_by_link_text('Pages').click()
    browser.find_element_by_id('pageManagerTitleInput').send_keys('pro')
    browser.find_element_by_class_name('bi').click()
    browser.find_element_by_link_text('Pages').click()
    browser.find_element_by_id('pageManagerTitleInput').send_keys('ecom')
    browser.find_element_by_class_name('bi').click()
    browser.find_element_by_link_text('Settings').click()
    time.sleep(5)
    WebDriverWait(browser, 30).until(lambda d : d.find_element_by_name('site_title')).clear()
    browser.find_element_by_name('site_title').send_keys('Test Site')
    browser.find_element_by_css_selector('div#saveProperties img').click()

def pro_test():
    time.sleep(10)
    try:
        WebDriverWait(browser, 10).until(lambda d : d.find_element_by_link_text(dom)).click()
    except TimeoutException:
        browser.find_element_by_css_selector('iframe').send_keys(Keys.ESCAPE)
    frame = browser.find_element_by_css_selector('iframe')
    browser.switch_to_frame(frame)
    browser.find_element_by_link_text('Pages').click()
    browser.find_element_by_xpath('//span[contains(.,"pro")] ').click()
    browser.find_element_by_xpath('//span[contains(.,"Edit Page")] ').click()
    browser.find_element_by_link_text('Multimedia').click()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_46196121'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_82970842'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_3971316'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    browser.find_element_by_link_text('More').click()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_48408403'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    browser.find_element_by_name('hourtown_email').send_keys('seleniumhumantwo@bluehost.com')
    browser.find_element_by_css_selector('img#lightbox_submitbtn').click()

def ecom_test():
    frame = browser.find_element_by_css_selector('iframe')
    browser.switch_to_frame(frame)
    #browser.find_element_by_link_text('Pages').click()
    #browser.find_element_by_xpath('//span[contains(.,"ecom")] ').click()
    #browser.find_element_by_xpath('//span[contains(, "Edit Page")] ').click()
    browser.find_element_by_link_text('Revenue').click()
    time.sleep(3)
    chains = webdriver.ActionChains(browser)
    chains.drag_and_drop(browser.find_element_by_name('id_61719152'), browser.find_element_by_class_name('weebly-content-area')).perform()
    time.sleep(3)
    browser.find_element_by_id('merchant-radio-paypal').click()
    browser.find_element_by_css_selector('img#lightbox_submitbtn').click()
    #chains = webdriver.ActionChains(browser)
    #chains.drag_and_drop(browser.find_element_by_name('id_61719152'), browser.find_element_by_class_name('weebly-content-area')).perform()
    #time.sleep(3)
    #chains = webdriver.ActionChains(browser)
    #chains.drag_and_drop(browser.find_element_by_name('id_61719152'), browser.find_element_by_class_name('weebly-content-area')).perform()


def make_pages():
    print('coming soon')

def test_pages():
    browser.get('http://' + dom)
    browser.get_screenshot_as_file(path + '/page.png')

def get_to_weebly():
    time.sleep(20)
    if not(browser.find_elements_by_link_text(dom)):
        WebDriverWait(browser, 10).until(lambda d : d.find_element_by_id('icon-weebly')).click()        
        WebDriverWait(browser, 10).until(lambda d : d.find_element_by_class_name('domain_upgrade')).click()
        WebDriverWait(browser, 10).until(lambda d : d.find_element_by_css_selector('select.domain_upgrade option[value="{}"]'.format(dom))).click()
        browser.find_element_by_class_name('btn').click()
    else:
        try:
            WebDriverWait(browser, 10).until(lambda d : d.find_element_by_link_text(dom)).click()
        except TimeoutException:
            browser.find_element_by_css_selector('iframe').send_keys(Keys.ESCAPE)

def publish():
    browser.find_element_by_id('publishButton').click()
    time.sleep(30)    
    
    
home = os.environ['HOME']
etime = str(int(time.time()))
os.makedirs(home + '/testcaps/'+ etime)
path = (home + '/testcaps/'+ etime)
domain = 'qa-' + etime
browser = webdriver.Firefox()
browser.set_page_load_timeout(30)
chains = webdriver.ActionChains(browser)
users = User(browser)
users.login()
signup()
wait_for_signup()
custid,user,box,ip,dom = cpm_get_info()
print('Signup Complete')
#verify_account()
print("The account is verified the domain is " + dom + "\n The custid is " +custid + "\n The Username is " + user +"\n IP adress is " + ip + "\n Temp url is http://" + ip + '/' + user + "\n")
browser.find_element_by_link_text('cPanel').click()
handles = browser.window_handles
browser.switch_to_window(handles[1])
get_to_weebly()
non_pro_test()
print('Upgrading to Pro')
upgrade('pro')
time.sleep(90)
get_to_weebly()
print('Testing Pro features')
pro_test()
print('Upgrading to ecom package')
upgrade('ecom')
time.sleep(90)
get_to_weebly()
print('Testing ecom package')
ecom_test()
publish()
