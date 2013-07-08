import time
from selenium.webdriver.common.keys import Keys
from simplescripts import SS
from selenium import webdriver

class TPTest():
    def __init__(self, selenium, path, etime, ip, user, dom, isbeta):
        self.selenium = selenium
        self.path = path
        self.etime = time
        self.ip = ip
        self.user = user
        self.domain = dom
        self.isbeta = isbeta
        
    def textpattern(self, phpv):
        if (self.isbeta == 0):
            #chains = webdriver.ActionChains(self.selenium)
            #chains.key_down(Keys.COMMAND)
            self.selenium.find_element_by_id('item_simplescripts-sb').click() #send_keys(Keys.CONTROL + "N")
            #chains.key_up(Keys.COMMAND)
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://www." +self.domain+ "/Textpattern/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('site-info')):
                print('Textpattern not installed to /Textpattern Directory installing')
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('Textpattern', 5, self.domain)
                self.selenium.get("http://www." +self.domain+ "/Textpattern/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + 'tp1-' + phpv + '.png')
            self.selenium.get("http://www."+self.domain+"/Textpattern/textpattern/index.php")
            time.sleep(10)
            self.selenium.save_screenshot(self.path + "tp2-" + phpv + ".png")
            self.selenium.find_element_by_name('p_userid').clear()
            self.selenium.find_element_by_name('p_userid').send_keys('admin')
            self.selenium.find_element_by_name('p_password').clear()
            self.selenium.find_element_by_name('p_password').send_keys('Test1234')
            self.selenium.find_element_by_class_name('publish').click()
            self.selenium.save_screenshot(self.path + "tp3-" + phpv + ".png")
            time.sleep(10)
            #self.selenium.get("http://www." + self.domain + "/WordPress/wp-login.php?action=logout")
            self.selenium.find_element_by_link_text('Logout').click()
            time.sleep(10)
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/Textpattern/")
            self.selenium.save_screenshot(self.path + "tp4" + phpv + ".png")
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        else:
            self.selenium.find_element_by_id('item_simplescripts-sb').click()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/Textpattern/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('site-info')):
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('Textpattern', 5, self.domain)
                self.selenium.get("http://" + self.ip +"/~" + self.user + "/Textpattern/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + "tp1" + phpv + ".png")
            self.selenium.get("http://"+self.ip+"/~"+self.user+"/Textpattern/textpattern/index.php")
            self.selenium.save_screenshot(self.path + "tp2" + phpv + ".png")
            self.selenium.find_element_by_name('p_userid').clear()
            self.selenium.find_element_by_name('p_userid').send_keys('admin')
            self.selenium.find_element_by_name('p_password').clear()
            self.selenium.find_element_by_name('p_password').send_keys('Test1234')
            self.selenium.find_element_by_class_name('puplish').click()
            self.selenium.save_screenshot(self.path + "tp3" + phpv + ".png")
            #self.selenium.get("http://" + self.ip + "/~" + self.user + "/WordPress/wp-login.php?action=logout");
            self.selenium.find_element_by_link_text('Logout').click()
            time.sleep(10)
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        return