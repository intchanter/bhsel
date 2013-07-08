import time
from selenium.webdriver.common.keys import Keys
from simplescripts import SS
from selenium import webdriver

class JTest():
    def __init__(self, selenium, path, etime, ip, user, dom, isbeta):
        self.selenium = selenium
        self.path = path
        self.etime = time
        self.ip = ip
        self.user = user
        self.domain = dom
        self.isbeta = isbeta
        
    def joomla2(self, phpv):
        if (self.isbeta == 0):
            #chains = webdriver.ActionChains(self.selenium)
            #chains.key_down(Keys.COMMAND)
            self.selenium.find_element_by_id('item_simplescripts-sb').click() #send_keys(Keys.CONTROL + "N")
            #chains.key_up(Keys.COMMAND)
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://www." +self.domain+ "/Joomla2/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('logoheader')):
                print('Joomla 2 not installed to /Joomla2 Directory installing')
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('Joomla 2', 5, self.domain)
                self.selenium.get("http://www." +self.domain+ "/Joomla2/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + 'j21-' + phpv + '.png')
            self.selenium.get("http://www."+self.domain+"/Joomla2/administrator/")
            time.sleep(10)
            self.selenium.save_screenshot(self.path + "j22-" + phpv + ".png")
            self.selenium.find_element_by_name('username').clear()
            self.selenium.find_element_by_name('username').send_keys('admin')
            self.selenium.find_element_by_name('passwd').clear()
            self.selenium.find_element_by_name('passwd').send_keys('Test1234')
            self.selenium.find_element_by_partial_link_text('Log in').click()
            self.selenium.save_screenshot(self.path + "j23-" + phpv + ".png")
            time.sleep(10)
            #self.selenium.get("http://www." + self.domain + "/WordPress/wp-login.php?action=logout")
            self.selenium.find_element_by_partial_link_text('Log out').click()
            time.sleep(10)
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/Joomla2/")
            self.selenium.save_screenshot(self.path + "j24" + phpv + ".png")
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        else:
            self.selenium.find_element_by_id('item_simplescripts-sb').click()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/Joomla2/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('logoheader')):
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('Joomla 2', 5, self.domain)
                self.selenium.get("http://" + self.ip +"/~" + self.user + "/Joomla2/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + "j21" + phpv + ".png")
            self.selenium.get("http://"+self.ip+"/~"+self.user+"/Joomla2/administrator/")
            self.selenium.save_screenshot(self.path + "j22" + phpv + ".png")
            self.selenium.find_element_by_name('username').clear()
            self.selenium.find_element_by_name('username').send_keys('admin')
            self.selenium.find_element_by_name('passwd').clear()
            self.selenium.find_element_by_name('passwd').send_keys('Test1234')
            self.selenium.find_element_by_link_text('Log in').click()
            self.selenium.save_screenshot(self.path + "j23" + phpv + ".png")
            #self.selenium.get("http://" + self.ip + "/~" + self.user + "/WordPress/wp-login.php?action=logout");
            self.selenium.find_element_by_link_text('Log out').click()
            time.sleep(10)
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        return