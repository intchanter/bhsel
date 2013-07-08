import time
from selenium.webdriver.common.keys import Keys
from simplescripts import SS
from selenium import webdriver

class CHTest():
    def __init__(self, selenium, path, etime, ip, user, dom, isbeta):
        self.selenium = selenium
        self.path = path
        self.etime = time
        self.ip = ip
        self.user = user
        self.domain = dom
        self.isbeta = isbeta
        
    def chyrp(self, phpv):
        if (self.isbeta == 0):
            #chains = webdriver.ActionChains(self.selenium)
            #chains.key_down(Keys.COMMAND)
            self.selenium.find_element_by_id('item_simplescripts-sb').click() #send_keys(Keys.CONTROL + "N")
            #chains.key_up(Keys.COMMAND)
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://www." +self.domain+ "/ChyrpCMS/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('header_box')):
                print('ChyrpCMS not installed to /ChyrpCMS Directory installing')
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('Chyrp CMS', 5, self.domain)
                self.selenium.get("http://www." +self.domain+ "/ChyrpCMS/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + 'ch1-' + phpv + '.png')
            self.selenium.get("http://www."+self.domain+"/ChyrpCMS/?action=login")
            time.sleep(10)
            self.selenium.save_screenshot(self.path + "ch2-" + phpv + ".png")
            self.selenium.find_element_by_name('login').clear()
            self.selenium.find_element_by_name('login').send_keys('admin')
            self.selenium.find_element_by_name('password').clear()
            self.selenium.find_element_by_name('password').send_keys('Test1234')
            self.selenium.find_element_by_id('submit').click()
            self.selenium.save_screenshot(self.path + "ch3-" + phpv + ".png")
            time.sleep(10)
            #self.selenium.get("http://www." + self.domain + "/ChyrpCMS/wp-login.php?action=logout")
            self.selenium.find_element_by_link_text('Log Out').click()
            time.sleep(10)
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/ChyrpCMS/")
            self.selenium.save_screenshot(self.path + "wp4" + phpv + ".png")
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        else:
            self.selenium.find_element_by_id('item_simplescripts-sb').click()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/ChyrpCMS/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('site-info')):
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('Chyrp CMS', 5, self.domain)
                self.selenium.get("http://" + self.ip +"/~" + self.user + "/ChyrpCMS/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + "ch1" + phpv + ".png")
            self.selenium.get("http://"+self.ip+"/~"+self.user+"/ChyrpCMS/?action=login")
            self.selenium.save_screenshot(self.path + "ch2" + phpv + ".png")
            self.selenium.find_element_by_name('login').clear()
            self.selenium.find_element_by_name('login').send_keys('admin')
            self.selenium.find_element_by_name('password').clear()
            self.selenium.find_element_by_name('password').send_keys('Test1234')
            self.selenium.find_element_by_name('wp-submit').click()
            self.selenium.save_screenshot(self.path + "ch3" + phpv + ".png")
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/ChyrpCMS/?action=login");
            self.selenium.find_element_by_link_text('Log Out').click()
            time.sleep(10)
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        return