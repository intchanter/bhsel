import time
from selenium.webdriver.common.keys import Keys
from simplescripts import SS
from selenium import webdriver

class C5Test():
    def __init__(self, selenium, path, etime, ip, user, dom, isbeta):
        self.selenium = selenium
        self.path = path
        self.etime = time
        self.ip = ip
        self.user = user
        self.domain = dom
        self.isbeta = isbeta
        
    def concrete(self, phpv):
        if (self.isbeta == 0):
            #chains = webdriver.ActionChains(self.selenium)
            #chains.key_down(Keys.COMMAND)
            self.selenium.find_element_by_id('item_simplescripts-sb').click() #send_keys(Keys.CONTROL + "N")
            #chains.key_up(Keys.COMMAND)
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://www." +self.domain+ "/concrete5/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('container_24')):
                print('concrete5 not installed to /concrete5 Directory installing')
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('concrete5', 5, self.domain)
                self.selenium.get("http://www." +self.domain+ "/concrete5/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + 'cc1-' + phpv + '.png')
            self.selenium.get("http://www."+self.domain+"/concrete5/index.php/login")
            time.sleep(10)
            self.selenium.save_screenshot(self.path + "cc2-" + phpv + ".png")
            self.selenium.find_element_by_name('uName').clear()
            self.selenium.find_element_by_name('uName').send_keys('admin')
            self.selenium.find_element_by_name('uPassword').clear()
            self.selenium.find_element_by_name('uPassword').send_keys('Test1234')
            self.selenium.find_element_by_id('submit').click()
            self.selenium.save_screenshot(self.path + "cc3-" + phpv + ".png")
            time.sleep(10)
            #self.selenium.get("http://www." + self.domain + "/WordPress/wp-login.php?action=logout")
            self.selenium.find_element_by_link_text('Sign Out').click()
            time.sleep(10)
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/concrete5/")
            self.selenium.save_screenshot(self.path + "cc4" + phpv + ".png")
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        else:
            self.selenium.find_element_by_id('item_simplescripts-sb').click()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/concrete5/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('container_24')):
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('concrete5', 5, self.domain)
                self.selenium.get("http://" + self.ip +"/~" + self.user + "/concrete5/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + "cc1" + phpv + ".png")
            self.selenium.get("http://"+self.ip+"/~"+self.user+"/concrete5/index.php/login")
            self.selenium.save_screenshot(self.path + "cc2" + phpv + ".png")
            self.selenium.find_element_by_name('uName').clear()
            self.selenium.find_element_by_name('uName').send_keys('admin')
            self.selenium.find_element_by_name('uPassword').clear()
            self.selenium.find_element_by_name('uPassword').send_keys('Test1234')
            self.selenium.find_element_by_id('submit').click()
            self.selenium.save_screenshot(self.path + "cc3" + phpv + ".png")
#            self.selenium.get("http://" + self.ip + "/~" + self.user + "/concrete5/login.php?action=logout");
            self.selenium.find_element_by_link_text('Sign Out').click()
            time.sleep(10)
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        return