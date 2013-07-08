import time
from selenium.webdriver.common.keys import Keys
from simplescripts import SS
from selenium import webdriver

class FATest():
    def __init__(self, selenium, path, etime, ip, user, dom, isbeta):
        self.selenium = selenium
        self.path = path
        self.etime = time
        self.ip = ip
        self.user = user
        self.domain = dom
        self.isbeta = isbeta
        
    def front(self, phpv):
        if (self.isbeta == 0):
            #chains = webdriver.ActionChains(self.selenium)
            #chains.key_down(Keys.COMMAND)
            self.selenium.find_element_by_id('item_simplescripts-sb').click() #send_keys(Keys.CONTROL + "N")
            #chains.key_up(Keys.COMMAND)
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://www." +self.domain+ "/FrontAccounting/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('titletext')):
                print('Front Accounting not installed to /FrontAccounting Directory installing')
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('Front Accounting', 5, self.domain)
                self.selenium.get("http://www." +self.domain+ "/FrontAccounting/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + 'fa1-' + phpv + '.png')
            #self.selenium.get("http://www."+self.domain+"/FrontAccounting/wp-admin")
            #time.sleep(10)
            self.selenium.save_screenshot(self.path + "fa2-" + phpv + ".png")
            self.selenium.find_element_by_name('user_name_entry_field').clear()
            self.selenium.find_element_by_name('user_name_entry_field').send_keys('admin')
            self.selenium.find_element_by_name('password').clear()
            self.selenium.find_element_by_name('password').send_keys('Test1234')
            self.selenium.find_element_by_name('SubmitUser').click()
            self.selenium.save_screenshot(self.path + "fa3-" + phpv + ".png")
            time.sleep(10)
            #self.selenium.get("http://www." + self.domain + "/FrontAccounting/wp-login.php?action=logout")
            self.selenium.find_element_by_link_text('Logout').click()
            time.sleep(10)
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/FrontAccounting/")
            self.selenium.save_screenshot(self.path + "fa4" + phpv + ".png")
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        else:
            self.selenium.find_element_by_id('item_simplescripts-sb').click()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/FrontAccounting/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('loginscreen')):
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('Front Accounting', 5, self.domain)
                self.selenium.get("http://" + self.ip +"/~" + self.user + "/FrontAccounting/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + "fa1" + phpv + ".png")
            #self.selenium.get("http://"+self.ip+"/~"+self.user+"/FrontAccounting/wp-admin")
            self.selenium.save_screenshot(self.path + "fa2" + phpv + ".png")
            self.selenium.find_element_by_name('user_name_entry_field').clear()
            self.selenium.find_element_by_name('user_name_entry_field').send_keys('admin')
            self.selenium.find_element_by_name('password').clear()
            self.selenium.find_element_by_name('password').send_keys('Test1234')
            self.selenium.find_element_by_name('SubmitUser').click()
            self.selenium.save_screenshot(self.path + "fa3" + phpv + ".png")
            #self.selenium.get("http://" + self.ip + "/~" + self.user + "/FrontAccounting/wp-login.php?action=logout");
            self.selenium.find_element_by_link_text('Logout').click()
            time.sleep(10)
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        return