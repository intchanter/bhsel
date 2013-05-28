#!/usr/bin/env python

from cpanel.software.phpconfig import PhpConf
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os
import tarfile

home = os.environ['HOME']
etime = int(time.time())
os.makedirs(home + '/testcaps/'+ etime)
path = (home + '/testcaps/'+ etime)
domain = 'qa-' + etime
browser = webdriver.Firefox()
browser.get('http://www.bluehost.com')
browser.save_screenshot(path + '/signup1.png')
browser.find_element_by_css('img.signup_button').click()
browser.WebDriverWait(browser, 10).until(lambda d : d.find_element_by_css('img.signup_button')).click()
browser.save_screenshot(path + '/signup2.png')
browser.find_element_by_id('domain').clear_element()
browser.find_element_by_id('domain').send_keys_to_element(domain)
browser.find_element_by_xpath('//input[@value="Next"]').click()
browser.find_element_by_link('Employee Test Data').click()
browser.find_element_by_name('next').click()
browser.save_screenshot(path + '/signup3.png')
browser.find_element_by_id('buy_now').click()
browser.save_screenshot(path + '/signup4.png')
time.sleep(120)
browser.find_element_by_link('cPanel Manager')
browser.save_screenshot(path + '/cpm.png')
u = browser.find_element_by_class('subtitle').get_text()
(dom, custid, user, box, address) = u.split(' | ')
(ip) = address.split( )
print('http://' + ip +'/~' + user +'\n')
gettosimplescripts(browser)
phpv = '53s'
simplescripts(browser)
arg = {'browser': browser, 'path': path, 'etime': etime, 'ip': ip, 'user': user, 'domain': domain, 'isbeta': isbeta, 'phpv': phpv}
test(browser, args)
phpv = '54s'
args['phpv'] = phpv
print("Changing php to 5.4 Single php.ini\n")
updatephp(browser, phpv)
handles = browser.window_handles
browser.find_element_by_id('item_simplescripts-sb').click()
handles = browser.window_handles
browser.switch_to_window(handles[2])
test(browser, args)
browser.switch_to_window(handles[0])
browser.find_element_by_link('phpMyAdmin').click
handles = browser.window_handles
browser.switch_to_window(handles[2])
time.sleep(20)
browser.save_screenshot(path + '/phpmyadmin.png')
print('Test Complete\n')
print('Zipping screenshots')
compressTar = tarfile.open(path+etime+".tar", "w:gz")
compressTar.add(path+etime+"/")
compressTar.close()
print('<a href='=path+etime+'.tar> Click here to download<a>\n')


def gettosimplescripts(browser):
    browser.find_element_by_link('cPanel').click()
    handles = browser.windows_handles
    browser.switch_to_window(handles[1])
    phpv = '53s'
    print('Changing php version to 5.3 Single php.ini\n')
    updatephp(browser, phpv)
    browser.find_element_by_id('item_simplescripts-sb').click
    time.wait(20)
    handles = browser.window_handles
    browser.switch_to_windows(handles[2])
    if browser.find_elements_by_link('My Installs'):
        print('Simple Scripts loaded on first try\n')
    else:
        browser.refesh()
        time.wait(20)
        if browser.find_elements_by_link('My Installs'):
            print('Simple Scripts loaded on second try\n')
        else:
            browser.refresh()
            time.wait(20)
            if browser.find_elements_by_link('My Installs'):
                print('Simple Scripts loaded on third try\n')
            else:
                die('Simple scripts failed to load after 3 tries!')

def updatephp(browser, phpv):
    version = {'52': 'php5', '52s': 'php5s', '52f': 'php5cgi', '53': 'php53', '53s': 'php53s', '54': 'php54'}
    handles = browser.get_window_handles
    browser.switch_to_window(handles[1])
    browser.find_element_by_id('item_php-config').click()
    browser.WebDriverWait(browser, 10).until(lambda d : d.browser.find_element_by_css('input[value='+version[phpv]']')).click()
    browser.find_element_by_css('input[value="SAVE CHANGES"]').click()
    browser.WebDriverWait(browser, 10).until(lambda d : d.browser.find_element_by_link('cPanel').click()

def simplescripts(browser):
    print('Installing Wordpress\n')
    install_script('Wordpress')
    print('Installing Joomla 2\n')
    install_script('Joomla 2')
    print('Installing Prestashop\n')
    install_script('Prestashop')
    print('Installing Concrete 5\n')
    install_script('concrete5')
    print('Installing MediaWiki\n')
    install_script('MediaWiki')
    print('Installing PHPBB\n')
    install_script('phpBB')
    print('Installing Drupal\n')
    install_script('Drupal')
    print('Installing b2evolution\n')
    install_script('b2evolution')
    print('Installing Chyrp CMS\n')
    install_script('Chyrp CMS')
    print('Installing Croogo\n')
    install_script('Croogo')
    print('Installing Geeklog\n')
    install_script('Geeklog')
    print('Installing Textpattern\n')
    install_script('Textpattern')
    print("Installing Noah's Classifieds\n")
    install_script("Noah's Classifieds")
    print('Installing Feng')
    install_script('Feng')
    print('Installing Front Accounting\n')
    install_script('Front Accounting')

def test:
    