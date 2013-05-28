from weebly import Test
from simplescripts import SS
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from testuser import User
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from wordpress import WPTest
from cpanel.software.phpconfig import PhpConf
import time
import os

isbeta = 0
home = os.environ['HOME']
etime = str(int(time.time()))
domain = 'qa-' + etime
browser = webdriver.Firefox()
browser.set_page_load_timeout(40)
path = (home + '/testcaps/'+ etime)
os.makedirs(home + '/testcaps/'+ etime)
users = User(browser)
users.login()
test = Test(browser, etime , home, path, domain)
test.signup()
test.wait_for_signup()
custid,user,box,ip,dom = test.cpm_get_info()
print('Signup Complete')
#verify_account()
print("The account is verified the domain is " + dom + "\n The custid is " +custid + "\n The Username is " + user +"\n IP adress is " + ip + "\n Temp url is http://" + ip + '/' + user + "\n")
browser.find_element_by_link_text('cPanel').click()
handles = browser.window_handles
browser.switch_to_window(handles[1])
phpver = PhpConf(browser)
ver = '53'
phpver.phpv(ver)
#simple = SS(browser)
#simple.get_to_simplescripts()
#simple.install_script('WordPress', 5)
wptest = WPTest(browser, path, etime, ip, user, dom, isbeta)
wptest.wordpress(ver)
phpv = '54'
phpver.phpv(ver)
wptest.wordpress(ver)
test.tar_screenshots()
print("Test complete you can get your screenshots at "+ path +'/'+ etime +".tar")