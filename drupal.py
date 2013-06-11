import time
from selenium.webdriver.common.keys import Keys
from simplescripts import SS
from selenium import webdriver

class DTest():
    def __init__(self, selenium, path, etime, ip, user, dom, isbeta):
        self.selenium = selenium
        self.path = path
        self.etime = time
        self.ip = ip
        self.user = user
        self.domain = dom
        self.isbeta = isbeta
        
    def Drupal7(self, phpv):
        if (self.isbeta == 0):
            #chains = webdriver.ActionChains(self.selenium)
            #chains.key_down(Keys.COMMAND)
            self.selenium.find_element_by_id('item_simplescripts-sb').click() #send_keys(Keys.CONTROL + "N")
            #chains.key_up(Keys.COMMAND)
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://www." +self.domain+ "/Drupal7/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_link_text('Home')):
                print('Drupal7 not installed to /Drupal7 Directory installing')
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('Drupal 7', 5)
                self.selenium.get("http://www." +self.domain+ "/Drupal7/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + 'dr1-' + phpv + '.png')
            #self.selenium.get("http://www."+self.domain+"/Drupal7/admin.php")
            time.sleep(10)
            self.selenium.save_screenshot(self.path + "dr2-" + phpv + ".png")
            self.selenium.find_element_by_name('name').clear()
            self.selenium.find_element_by_name('name').send_keys('admin')
            self.selenium.find_element_by_name('pass').clear()
            self.selenium.find_element_by_name('pass').send_keys('Test1234')
            self.selenium.find_element_by_id('edit-submit').click()
            self.selenium.save_screenshot(self.path + "dr3-" + phpv + ".png")
            time.sleep(10)
            self.selenium.find_element_by_link_text('Log out').click()
            #self.selenium.find_element_by_link_text('log out').click()
            time.sleep(10)
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/Drupal7/")
            self.selenium.save_screenshot(self.path + "dr4" + phpv + ".png")
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        else:
            self.selenium.find_element_by_id('item_simplescripts-sb').click()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/Drupal7/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_link_text('Home')):
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('Drupal 7', 5)
                self.selenium.get("http://" + self.ip +"/~" + self.user + "/Drupal7/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + "dr1" + phpv + ".png")
            self.selenium.get("http://"+self.ip+"/~"+self.user+"/Drupal7/admin.php")
            self.selenium.save_screenshot(self.path + "dr2" + phpv + ".png")
            self.selenium.find_element_by_name('x').clear()
            self.selenium.find_element_by_name('x').send_keys('admin')
            self.selenium.find_element_by_name('q').clear()
            self.selenium.find_element_by_name('q').send_keys('Test1234')
            self.selenium.find_element_by_id('edit-submit').click()
            self.selenium.save_screenshot(self.path + "dr3" + phpv + ".png")
            #self.selenium.get("http://" + self.ip + "/~" + self.user + "/Drupal7/htsrv/login.php?action=logout");
            self.selenium.find_element_by_link_text('Log out').click()
            time.sleep(10)
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        return