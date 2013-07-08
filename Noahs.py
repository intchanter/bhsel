import time
from selenium.webdriver.common.keys import Keys
from simplescripts import SS
from selenium import webdriver

class NTest():
    def __init__(self, selenium, path, etime, ip, user, dom, isbeta):
        self.selenium = selenium
        self.path = path
        self.etime = time
        self.ip = ip
        self.user = user
        self.domain = dom
        self.isbeta = isbeta
        
    def noahs(self, phpv):
        if (self.isbeta == 0):
            #chains = webdriver.ActionChains(self.selenium)
            #chains.key_down(Keys.COMMAND)
            self.selenium.find_element_by_id('item_simplescripts-sb').click() #send_keys(Keys.CONTROL + "N")
            #chains.key_up(Keys.COMMAND)
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://www." +self.domain+ "/NoahsClassifieds/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('site-info')):
                print('Noahs Classifieds not installed to /NoahsClassifieds Directory installing')
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script("Noah's Classifieds", 5, self.domain)
                self.selenium.get("http://www." +self.domain+ "/NoahsClassifieds/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + 'no1-' + phpv + '.png')
            self.selenium.get("http://www."+self.domain+"/NoahsClassifieds/index.php?user/login_form/")
            time.sleep(10)
            self.selenium.save_screenshot(self.path + "no2-" + phpv + ".png")
            self.selenium.find_element_by_id('name').clear()
            self.selenium.find_element_by_id('name').send_keys('admin')
            self.selenium.find_element_by_id('password').clear()
            self.selenium.find_element_by_id('password').send_keys('Test1234')
            self.selenium.find_element_by_name('gsubmit').click()
            self.selenium.save_screenshot(self.path + "no3-" + phpv + ".png")
            time.sleep(10)
            #self.selenium.get("http://www." + self.domain + "/NoahsClassifieds/wp-login.php?action=logout")
            if (self.selenium.find_elements_by_link_text('Logout')):
                self.selenium.find_element_by_link_text('Logout').click()
            else:
                self.selenium.refresh()
                self.selenium.switch_to_alert().accept()
                time.sleep(5)
                self.selenium.find_element_by_link_text('Logout').click()
            time.sleep(10)
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/NoahsClassifieds/")
            self.selenium.save_screenshot(self.path + "no4" + phpv + ".png")
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        else:
            self.selenium.find_element_by_id('item_simplescripts-sb').click()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/NoahsClassifieds/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('site-info')):
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script("Noah's Classifieds", 5, self.domain)
                self.selenium.get("http://" + self.ip +"/~" + self.user + "/NoahsClassifieds/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + "no1" + phpv + ".png")
            self.selenium.get("http://"+self.ip+"/~"+self.user+"/NoahsClassifieds/index.php?user/login_form/")
            self.selenium.save_screenshot(self.path + "no2" + phpv + ".png")
            self.selenium.find_element_by_id('name').clear()
            self.selenium.find_element_by_id('name').send_keys('admin')
            self.selenium.find_element_by_id('password').clear()
            self.selenium.find_element_by_id('password').send_keys('Test1234')
            self.selenium.find_element_by_name('gsubmit').click()
            self.find_element_by_link_text('Logout')
            self.selenium.save_screenshot(self.path + "wp3" + phpv + ".png")
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/NoahsClassifieds/wp-login.php?action=logout");
            self.selenium.find_element_by_link_text('Logout').click()
            time.sleep(10)
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        return