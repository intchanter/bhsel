from weebly import Test
from simplescripts import SS
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from testuser import User
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from wordpress import WPTest
from b2evolution import B2Test
from drupal import DTest
from prestashop import PSTest
from Noahs import NTest
from front import FATest
from chyrp import CHTest
from croogo import CRTest
from phpbb import PHTest
from concrete import C5Test
from mediawiki import MWTest
from textpattern import TPTest
from joomla import JTest
from cpanel.software.phpconfig import PhpConf
import config
import time
import os
import utility
isbeta = 0
home = os.environ['HOME']
etime = str(int(time.time()))
domain = 'qa-' + etime
browser = webdriver.Firefox()
config.config = config.Config(browser, 'http://www.bluehost.com/', 'bluehost')
browser.set_page_load_timeout(40)
path = (home + '/testcaps/'+ etime)
os.makedirs(home + '/testcaps/'+ etime)
users = User(browser)
users.login()
test = Test(browser, etime , home, path, domain)
utility.basic_signup(domain)
#test.signup()
#test.wait_for_signup()
custid,user,box,ip,dom = test.cpm_get_info()
print('Signup Complete')
#verify_account()
print("The account is verified the domain is " + dom + "\n The custid is " +custid + "\n The Username is " + user +"\n IP adress is " + ip + "\n Temp url is http://" + ip + '/' + user + "\n")
browser.find_element_by_link_text('cPanel').click()
handles = browser.window_handles
browser.switch_to_window(handles[1])
phpver = PhpConf(browser)
ver = '53'
time.sleep(10)
phpver.phpv(ver)
#simple = SS(browser)
#simple.get_to_simplescripts()
#simple.install_script('WordPress', 5)
wptest = WPTest(browser, path, etime, ip, user, dom, isbeta)
betest = B2Test(browser, path, etime, ip, user, dom, isbeta)
dtest = DTest(browser, path, etime, ip, user, dom, isbeta)
pstest = PSTest(browser, path, etime, ip, user, dom, isbeta)
ntest = NTest(browser, path, etime, ip, user, dom, isbeta)
ftest = FATest(browser, path, etime, ip, user, dom, isbeta)
chtest = CHTest(browser, path, etime, ip, user, dom, isbeta)
crtest = CRTest(browser, path, etime, ip, user, dom, isbeta)
crtest = CRTest(browser, path, etime, ip, user, dom, isbeta)
phtest = PHTest(browser, path, etime, ip, user, dom, isbeta)
c5test = C5Test(browser, path, etime, ip, user, dom, isbeta)
mwtest = MWTest(browser, path, etime, ip, user, dom, isbeta)
tptest = TPTest(browser, path, etime, ip, user, dom, isbeta)
jtest = JTest(browser, path, etime, ip, user, dom, isbeta)
jtest.joomla2(ver)
#tptest.textpattern(ver)
#mwtest.mediawiki(ver)
#phtest.phpbb(ver)
##ntest.noahs(ver)
#c5test.concrete(ver)
#crtest.croogo(ver)
#chtest.chyrp(ver)
#ftest.front(ver)
#wptest.wordpress(ver)
#betest.b2evolution(ver)
#dtest.Drupal7(ver)
#pstest.prestashop(ver)
ver = '54'
phpver.phpv(ver)
jtest.joomla2(ver)
#tptest.textpattern(ver)
#mwtest.mediawiki(ver)
#wptest.wordpress(ver)
#betest.b2evolution(ver)
#dtest.Drupal7(ver)
#ftest.front(ver)
#pstest.prestashop(ver)
#ntest.noahs(ver)
#chtest.chyrp(ver)
#crtest.croogo(ver)
#phtest.phpbb(ver)
#c5test.concrete(ver)
test.tar_screenshots()
print("Test complete you can get your screenshots at "+ path +'/'+ etime +".tar")
