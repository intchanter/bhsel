#!/usr/bin/env python
from weebly import Test
from selenium import webdriver
from testuser import User
import time
import os

home = os.environ['HOME']
etime = str(int(time.time()))
os.makedirs(home + '/testcaps/'+ etime)
path = (home + '/testcaps/'+ etime)
domain = 'qa-' + etime
browser = webdriver.Firefox()
browser.set_page_load_timeout(30)
chains = webdriver.ActionChains(browser)
test = Test(browser, etime , home, path, domain)
users = User(browser)
#browser.find_element_by_class_name('weebly-content-area') = browser.find_element_by_class_name('weebly-content-area')
users.login()
test.signup()
test.wait_for_signup()
custid,user,box,ip,dom = test.cpm_get_info()
print('Signup Complete')
#verify_account()
print("The account is verified the domain is " + dom + "\n The custid is " +custid + "\n The Username is " + user +"\n IP adress is " + ip + "\n Temp url is http://" + ip + '/' + user + "\n")
browser.find_element_by_link_text('cPanel').click()
handles = browser.window_handles
browser.switch_to_window(handles[1])
test.get_to_weebly(dom)
test.non_pro_test()
print('Upgrading to Pro')
test.upgrade('pro', users)
time.sleep(90)
test.get_to_weebly(dom)
print('Testing Pro features')
test.pro_test()
print('Upgrading to ecom package')
test.upgrade('ecom', users)
time.sleep(90)
test.get_to_weebly(dom)
print('Testing ecom package')
test.ecom_test()
test.publish()
print ('Going to published Page')
test.test_pages(dom)
print ('Creating tar for screenshots')
test.tar_screenshots()
print("Test complete you can get your screenshots at "+ path +'/'+ etime +".tar")