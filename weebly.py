#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import tarfile

class Test(): 
    def __init__ (self, selenium, etime , home, path, domain):
        self.selenium = selenium
        self.etime = etime
        self.home = home
        self.path = path
        self.domain = domain
        
    def tar_screenshots(self):
        #Create Tar file
        tFile = tarfile.open(self.home + '/testcaps/' +self.etime+ '.tar', 'w')
        #Add directory contents to tar file
        tFile.add(self.path)
        #for f in files:
        #    tFile.add(f)

        #List files in tar
        for f in tFile.getnames():
            print ("Added %s" % f)

        tFile.close()
    
    def cpm_get_info(self):
        u = self.selenium.find_element_by_class_name('subtitle').text
        (dom2, custid, user, box, address) = u.split(' | ')
        (ip, junk) = address.split( )
        (junk,dom) = dom2.split( )
        return (custid, user, box, ip, dom)

    def wait_for_signup(self):
        if not (self.selenium.find_elements_by_link_text('cPanel')):
            while not (self.selenium.find_elements_by_link_text('cPanel')):
                time.sleep(150)
                self.selenium.refresh()
                input('press enter when cpanel is installed')
                return
        else:
            input('press enter when cpanel is installed')
        return
    def upgrade(self, kind ,users):
        self.selenium.switch_to_default_content()
        self.selenium.find_element_by_css_selector('div#header_upgrade img').click()
        time.sleep(3)
        if self.selenium.find_elements_by_link_text('Select Domain'):
            self.selenium.find_element_by_link_text('Select Domain').click()
        #else:
        #self.selenium.find_element_by_link_text(dom).click()
        if (kind == 'pro'):
            WebDriverWait(self.selenium, 10).until(lambda d : d.find_element_by_name('add_proaccount')).click()
        elif (kind == 'ecom'):
            WebDriverWait(self.selenium, 10).until(lambda d : d.find_element_by_name('add_ecommerce')).click()
        self.selenium.find_element_by_css_selector('.btn_primary.add_to_cart').click()
        self.selenium.find_element_by_name('CVV2_EXISTING').send_keys('349')
        self.selenium.find_element_by_css_selector('button.btn_primary').click()
        self.selenium.switch_to_alert().accept()
        time.sleep(3)
        if self.selenium.find_elements_by_class_name('login_username'):
            users.login_single_page()
            self.selenium.find_element_by_css_selector('button.btn_primary').click()
            self.selenium.switch_to_alert().accept()
        while not self.selenium.find_elements_by_link_text('Click here'):
            time.sleep(5)
            if (self.selenium.find_elements_by_id('start_button2')):
                self.selenium.find_element_by_id('start_button2').click()
        self.selenium.find_element_by_link_text('Click here').click()
        WebDriverWait(self.selenium, 10).until(lambda d : d.find_element_by_link_text('Hosting')).click()

    def signup(self):
        self.selenium.get('http://www.bluehost.com')
        self.selenium.get_screenshot_as_file(self.path + '/signup1.png')
        self.selenium.find_element_by_css_selector('img.signup_button').click()
        #WebDriverWait(self.selenium, 10).until(lambda d : d.find_element_by_css_selector('img.signup_button')).click()
        WebDriverWait(self.selenium, 20).until(lambda d : d.find_element_by_id('domain')).clear()
        self.selenium.get_screenshot_as_file(self.path + '/signup2.png')
        self.selenium.find_element_by_id('domain').send_keys(self.domain)
        self.selenium.find_element_by_xpath('//input[@value="Next"]').click()
        self.selenium.find_element_by_link_text('Employee Test Data "Approved"').click()
        self.selenium.find_element_by_name('next').click()
        self.selenium.get_screenshot_as_file(self.path + '/signup3.png')
        self.selenium.find_element_by_id('buy_now').click()
        self.selenium.get_screenshot_as_file(self.path + '/signup4.png')
        self.selenium.find_element_by_link_text('cPanel Manager').click()
        self.selenium.get_screenshot_as_file(self.path + '/cpm.png')


    def non_pro_test(self):
        time.sleep(20)
        frame = self.selenium.find_element_by_css_selector('iframe')
        self.selenium.switch_to_frame(frame)
        chains = webdriver.ActionChains(self.selenium)
        WebDriverWait(self.selenium, 30).until(lambda d : d.find_element_by_name('id_58462494'))
        chains.drag_and_drop(self.selenium.find_element_by_name('id_58462494'), self.selenium.find_element_by_id('empty-message-inner')).perform()
        time.sleep(3)
        self.selenium.find_element_by_id('logo').click()
        chains = webdriver.ActionChains(self.selenium)
        time.sleep(3)
        chains.click_and_hold(self.selenium.find_element_by_name('id_20731748'))
        time.sleep(3)
        chains.release(self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        #chains.drag_and_drop(self.selenium.find_element_by_name('id_20731748'), self.selenium.find_element_by_class_name('element-box-contents')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        time.sleep(3)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_87358824'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_62850560'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_44785763'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_51424376'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_92495494'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_45444132'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_59396708'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        self.selenium.find_element_by_link_text('Multimedia').click()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_18362204'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_31574711'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        self.selenium.find_element_by_link_text('Continue').click()
        self.selenium.find_element_by_class_name('weebly-dialog-close').click()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_46196121'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        handles = self.selenium.window_handles
        self.selenium.switch_to_window(handles[2])
        self.selenium.get_screenshot_as_file(self.path + '/upsell.png')
        self.selenium.close()
        self.selenium.switch_to_window(handles[1])
        frame = self.selenium.find_element_by_css_selector('iframe')
        self.selenium.switch_to_frame(frame)
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        time.sleep(3)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_64190838'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_42844424'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_85353141'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_8893461'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        self.selenium.find_element_by_link_text('More').click()
        self.selenium.find_element_by_link_text('Layout').click()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_79078446'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        self.selenium.find_element_by_link_text('Misc').click()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_62317151'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        self.selenium.find_element_by_link_text('Forms').click()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_20040879'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_42391650'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        self.selenium.find_element_by_link_text('Design').click()
        self.selenium.find_element_by_id('theme_417534755793912073').click()
        self.selenium.find_element_by_id('theme_189529082218988161').click()
        self.selenium.find_element_by_id('theme_753078197207386506').click()
        self.selenium.find_element_by_id('theme_701731089317975641').click()
        self.selenium.find_element_by_link_text('Pages').click()
        self.selenium.find_element_by_id('pageManagerTitleInput').send_keys('pro')
        self.selenium.find_element_by_class_name('bi').click()
        self.selenium.find_element_by_link_text('Pages').click()
        self.selenium.find_element_by_id('pageManagerTitleInput').send_keys('ecom')
        self.selenium.find_element_by_class_name('bi').click()
        self.selenium.find_element_by_link_text('Settings').click()
        time.sleep(5)
        WebDriverWait(self.selenium, 30).until(lambda d : d.find_element_by_name('site_title')).clear()
        self.selenium.find_element_by_name('site_title').send_keys('Test Site')
        self.selenium.find_element_by_css_selector('div#saveProperties img').click()

    def pro_test(self):
        time.sleep(10)
        #try:
        #   WebDriverWait(self.selenium, 10).until(lambda d : d.find_element_by_link_text(dom)).click()
        #except TimeoutException:
        #   self.selenium.find_element_by_css_selector('iframe').send_keys(Keys.ESCAPE)
        frame = self.selenium.find_element_by_css_selector('iframe')
        self.selenium.switch_to_frame(frame)
        #self.selenium.find_element_by_link_text('Pages').click()
        #self.selenium.find_element_by_xpath('//span[contains(.,"pro")] ').click()
        #self.selenium.find_element_by_xpath('//span[contains(.,"Edit Page")] ').click()
        try:
            self.selenium.find_element_by_link_text('Multimedia').click()
        except TimeoutException:
            self.selenium.find_element_by_class_name('weebly-content-area').send_keys(Keys.ESCAPE)
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_46196121'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_82970842'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_3971316'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        self.selenium.find_element_by_link_text('More').click()
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_48408403'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        self.selenium.find_element_by_name('hourtown_email').send_keys('seleniumhumantwo@bluehost.com')
        self.selenium.find_element_by_css_selector('img#lightbox_submitbtn').click()

    def ecom_test(self):
        time.sleep(10)
        frame = self.selenium.find_element_by_css_selector('iframe')
        self.selenium.switch_to_frame(frame)
        #self.selenium.find_element_by_link_text('Pages').click()
        #self.selenium.find_element_by_xpath('//span[contains(.,"ecom")] ').click()
        #self.selenium.find_element_by_xpath('//span[contains(, "Edit Page")] ').click()
        try:
            self.selenium.find_element_by_link_text('Revenue').click()
        except TimeoutException:
            self.selenium.find_element_by_class_name('weebly-content-area').send_keys(Keys.ESCAPE)
        time.sleep(3)
        chains = webdriver.ActionChains(self.selenium)
        chains.drag_and_drop(self.selenium.find_element_by_name('id_61719152'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        time.sleep(3)
        self.selenium.find_element_by_id('merchant-radio-paypal').click()
        self.selenium.find_element_by_css_selector('img#lightbox_submitbtn').click()
        #chains = webdriver.ActionChains(self.selenium)
        #chains.drag_and_drop(self.selenium.find_element_by_name('id_61719152'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()
        #time.sleep(3)
        #chains = webdriver.ActionChains(self.selenium)
        #chains.drag_and_drop(self.selenium.find_element_by_name('id_61719152'), self.selenium.find_element_by_class_name('weebly-content-area')).perform()


    def make_pages(self):
        print('coming soon')

    def test_pages(self, dom):
        self.selenium.get('http://' + dom)
        time.sleep(3)
        self.selenium.get_screenshot_as_file(self.path + '/page.png')

    def get_to_weebly(self, dom):
        WebDriverWait(self.selenium, 10).until(lambda d : d.find_element_by_id('icon-weebly')).click() 
        time.sleep(15)
        if not(self.selenium.find_elements_by_link_text(dom)):
            WebDriverWait(self.selenium, 10).until(lambda d : d.find_element_by_class_name('domain_upgrade')).click()
            WebDriverWait(self.selenium, 10).until(lambda d : d.find_element_by_css_selector('select.domain_upgrade option[value="{}"]'.format(dom))).click()
            self.selenium.find_element_by_class_name('btn').click()
        else:
            try:
                WebDriverWait(self.selenium, 10).until(lambda d : d.find_element_by_link_text(dom)).click()
            except TimeoutException:
                self.selenium.find_element_by_css_selector('iframe').send_keys(Keys.ESCAPE)
                print ("Timed out Logging in.  This is a current Weebly Bug and coded to account for it.")
    def publish(self):
        self.selenium.find_element_by_id('publishButton').click()
        time.sleep(30)    
    
    
