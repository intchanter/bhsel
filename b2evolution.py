import time
from selenium.webdriver.common.keys import Keys
from simplescripts import SS
from selenium import webdriver

class B2Test():
    def __init__(self, selenium, path, etime, ip, user, dom, isbeta):
        self.selenium = selenium
        self.path = path
        self.etime = time
        self.ip = ip
        self.user = user
        self.domain = dom
        self.isbeta = isbeta
        
    def b2evolution(self, phpv):
        if (self.isbeta == 0):
            #chains = webdriver.ActionChains(self.selenium)
            #chains.key_down(Keys.COMMAND)
            self.selenium.find_element_by_id('item_simplescripts-sb').click() #send_keys(Keys.CONTROL + "N")
            #chains.key_up(Keys.COMMAND)
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://www." +self.domain+ "/b2evolution/blog1.php")
            time.sleep(5)
            if not (self.selenium.find_elements_by_link_text('Home')):
                print('b2evolution not installed to /b2evolution Directory installing')
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('b2evolution', 5)
                self.selenium.get("http://www." +self.domain+ "/b2evolution/blog1.php")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + 'be1-' + phpv + '.png')
            self.selenium.get("http://www."+self.domain+"/b2evolution/admin.php")
            time.sleep(10)
            self.selenium.save_screenshot(self.path + "be2-" + phpv + ".png")
            self.selenium.find_element_by_name('x').clear()
            self.selenium.find_element_by_name('x').send_keys('admin')
            self.selenium.find_element_by_name('q').clear()
            self.selenium.find_element_by_name('q').send_keys('Test1234')
            self.selenium.find_element_by_name('login_action[login]').click()
            self.selenium.save_screenshot(self.path + "be3-" + phpv + ".png")
            time.sleep(10)
            self.selenium.get("http://www." + self.domain + "/b2evolution/htsrv/login.php?action=logout")
            #self.selenium.find_element_by_link_text('log out').click()
            time.sleep(10)
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/b2evolution/blog1.php")
            self.selenium.save_screenshot(self.path + "be4" + phpv + ".png")
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        else:
            self.selenium.find_element_by_id('item_simplescripts-sb').click()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/b2evolution/blog1.php")
            time.sleep(5)
            if not (self.selenium.find_elements_by_link_text('Home')):
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('b2evolution', 5)
                self.selenium.get("http://" + self.ip +"/~" + self.user + "/b2evolution/blog1.php")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + "be1" + phpv + ".png")
            self.selenium.get("http://"+self.ip+"/~"+self.user+"/b2evolution/admin.php")
            self.selenium.save_screenshot(self.path + "be2" + phpv + ".png")
            self.selenium.find_element_by_name('x').clear()
            self.selenium.find_element_by_name('x').send_keys('admin')
            self.selenium.find_element_by_name('q').clear()
            self.selenium.find_element_by_name('q').send_keys('Test1234')
            self.selenium.find_element_by_name('login_action[login]').click()
            self.selenium.save_screenshot(self.path + "be3" + phpv + ".png")
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/b2evolution/htsrv/login.php?action=logout");
            #self.selenium.find_element_by_link_text('log Out').click()
            time.sleep(10)
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        return