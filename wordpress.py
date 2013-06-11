import time
from selenium.webdriver.common.keys import Keys
from simplescripts import SS
from selenium import webdriver

class WPTest():
    def __init__(self, selenium, path, etime, ip, user, dom, isbeta):
        self.selenium = selenium
        self.path = path
        self.etime = time
        self.ip = ip
        self.user = user
        self.domain = dom
        self.isbeta = isbeta
        
    def wordpress(self, phpv):
        if (self.isbeta == 0):
            #chains = webdriver.ActionChains(self.selenium)
            #chains.key_down(Keys.COMMAND)
            self.selenium.find_element_by_id('item_simplescripts-sb').click() #send_keys(Keys.CONTROL + "N")
            #chains.key_up(Keys.COMMAND)
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://www." +self.domain+ "/WordPress/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('site-info')):
                print('Wordpress not installed to /WordPress Directory installing')
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('WordPress', 5)
                self.selenium.get("http://www." +self.domain+ "/WordPress/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + 'wp1-' + phpv + '.png')
            self.selenium.get("http://www."+self.domain+"/WordPress/wp-admin")
            time.sleep(10)
            self.selenium.save_screenshot(self.path + "wp2-" + phpv + ".png")
            self.selenium.find_element_by_name('log').clear()
            self.selenium.find_element_by_name('log').send_keys('seleniumhumantwo@bluehost.com')
            self.selenium.find_element_by_name('pwd').clear()
            self.selenium.find_element_by_name('pwd').send_keys('Test1234')
            self.selenium.find_element_by_name('wp-submit').click()
            self.selenium.save_screenshot(self.path + "wp3-" + phpv + ".png")
            time.sleep(10)
            self.selenium.get("http://www." + self.domain + "/WordPress/wp-login.php?action=logout")
            self.selenium.find_element_by_link_text('log out').click()
            time.sleep(10)
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/WordPress/")
            self.selenium.save_screenshot(self.path + "wp4" + phpv + ".png")
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        else:
            self.selenium.find_element_by_id('item_simplescripts-sb').click()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/WordPress/")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('site-info')):
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('WordPress', 5)
                self.selenium.get("http://" + self.ip +"/~" + self.user + "/WordPress/")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + "wp1" + phpv + ".png")
            self.selenium.get("http://"+self.ip+"/~"+self.user+"/WordPress/wp-admin")
            self.selenium.save_screenshot(self.path + "wp2" + phpv + ".png")
            self.selenium.find_element_by_name('log').clear()
            self.selenium.find_element_by_name('log').send_keys('seleniumhumantwo@bluehost.com')
            self.selenium.find_element_by_name('pwd').clear()
            self.selenium.find_element_by_name('pwd').send_keys('Test1234')
            self.selenium.find_element_by_name('wp-submit').click()
            self.selenium.save_screenshot(self.path + "wp3" + phpv + ".png")
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/WordPress/wp-login.php?action=logout");
            self.selenium.find_element_by_link_text('log Out').click()
            time.sleep(10)
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        return