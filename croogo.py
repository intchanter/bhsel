import time
from selenium.webdriver.common.keys import Keys
from simplescripts import SS
from selenium import webdriver

class CRTest():
    def __init__(self, selenium, path, etime, ip, user, dom, isbeta):
        self.selenium = selenium
        self.path = path
        self.etime = time
        self.ip = ip
        self.user = user
        self.domain = dom
        self.isbeta = isbeta
        
    def croogo(self, phpv):
        if (self.isbeta == 0):
            #chains = webdriver.ActionChains(self.selenium)
            #chains.key_down(Keys.COMMAND)
            self.selenium.find_element_by_id('item_simplescripts-sb').click() #send_keys(Keys.CONTROL + "N")
            #chains.key_up(Keys.COMMAND)
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://www." +self.domain+ "/Croogo/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('container_16')):
                print('Croogo not installed to /Croogo Directory installing')
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('Croogo', 5, self.domain)
                self.selenium.get("http://www." +self.domain+ "/Croogo/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + 'cr1-' + phpv + '.png')
            self.selenium.get("http://www."+self.domain+"/Croogo/admin/")
            time.sleep(10)
            self.selenium.save_screenshot(self.path + "cr2-" + phpv + ".png")
            self.selenium.find_element_by_id('UserUsername').clear()
            self.selenium.find_element_by_id('UserUsername').send_keys('admin')
            self.selenium.find_element_by_id('UserPassword').clear()
            self.selenium.find_element_by_id('UserPassword').send_keys('Test1234')
            self.selenium.find_element_by_css_selector('button.btn').click()
            self.selenium.save_screenshot(self.path + "cr3-" + phpv + ".png")
            time.sleep(10)
            #self.selenium.get("http://www." + self.domain + "/WordPress/wp-login.php?action=logout")
            self.selenium.find_element_by_link_text('Log out').click()
            time.sleep(10)
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/Croogo/app/webroot")
            self.selenium.save_screenshot(self.path + "cr4" + phpv + ".png")
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        else:
            self.selenium.find_element_by_id('item_simplescripts-sb').click()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/Croogo/app/webroot")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('container_16')):
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('Croogo', 5, self.domain)
                self.selenium.get("http://" + self.ip +"/~" + self.user + "/Croogo/app/webroot")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + "cr1" + phpv + ".png")
            self.selenium.get("http://"+self.ip+"/~"+self.user+"/Croogo/admin/")
            self.selenium.save_screenshot(self.path + "cr2" + phpv + ".png")
            self.selenium.find_element_by_id('UserUsername').clear()
            self.selenium.find_element_by_id('UserUsername').send_keys('admin')
            self.selenium.find_element_by_id('UserPassword').clear()
            self.selenium.find_element_by_id('UserPassword').send_keys('Test1234')
            self.selenium.find_element_by_css_selector('button.btn').click()
            self.selenium.save_screenshot(self.path + "cr3" + phpv + ".png")
            #self.selenium.get("http://" + self.ip + "/~" + self.user + "/WordPress/wp-login.php?action=logout");
            self.selenium.find_element_by_link_text('Log out').click()
            time.sleep(10)
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        return