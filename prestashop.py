import time
from selenium.webdriver.common.keys import Keys
from simplescripts import SS
from selenium import webdriver

class PSTest():
    def __init__(self, selenium, path, etime, ip, user, dom, isbeta):
        self.selenium = selenium
        self.path = path
        self.etime = time
        self.ip = ip
        self.user = user
        self.domain = dom
        self.isbeta = isbeta
        
    def prestashop(self, phpv):
        if (self.isbeta == 0):
            #chains = webdriver.ActionChains(self.selenium)
            #chains.key_down(Keys.COMMAND)
            self.selenium.find_element_by_id('item_simplescripts-sb').click() #send_keys(Keys.CONTROL + "N")
            #chains.key_up(Keys.COMMAND)
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://www." +self.domain+ "/PrestaShop/index.php")
            time.sleep(5)
            if not (self.selenium.find_elements_by_id('index')):
                print('Prestashop not installed to /PrestaShop Directory installing')
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('PrestaShop', 5, self.domain)
                self.selenium.get("http://www." +self.domain+ "/PrestaShop/index.php")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + 'ps1-' + phpv + '.png')
            self.selenium.get("http://www."+self.domain+"/PrestaShop/psadmin/index.php")
            time.sleep(10)
            self.selenium.save_screenshot(self.path + "ps2-" + phpv + ".png")
            self.selenium.find_element_by_name('email').clear()
            self.selenium.find_element_by_name('email').send_keys('seleniumhumantwo@bluehost.com')
            self.selenium.find_element_by_name('passwd').clear()
            self.selenium.find_element_by_name('passwd').send_keys('Test1234')
            self.selenium.find_element_by_name('submitLogin').click()
            self.selenium.save_screenshot(self.path + "ps3-" + phpv + ".png")
            time.sleep(10)
            #self.selenium.get("http://www." + self.domain + "/WordPress/wp-login.php?action=logout")
            self.selenium.find_element_by_link_text('Logout').click()
            time.sleep(10)
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/PrestaShop/index.php")
            self.selenium.save_screenshot(self.path + "ps4" + phpv + ".png")
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        else:
            self.selenium.find_element_by_id('item_simplescripts-sb').click()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/PrestaShop/index.php")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('site-info')):
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('PrestaShop', 5, self.domain)
                self.selenium.get("http://" + self.ip +"/~" + self.user + "/PrestaShop/index.php")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + "ps1" + phpv + ".png")
            self.selenium.get("http://"+self.ip+"/~"+self.user+"/WordPress/wp-admin")
            self.selenium.save_screenshot(self.path + "ps2" + phpv + ".png")
            self.selenium.find_element_by_name('email').clear()
            self.selenium.find_element_by_name('email').send_keys('seleniumhumantwo@bluehost.com')
            self.selenium.find_element_by_name('passwd').clear()
            self.selenium.find_element_by_name('passwd').send_keys('Test1234')
            self.selenium.find_element_by_name('submitLogin').click()
            self.selenium.save_screenshot(self.path + "ps3" + phpv + ".png")
            #self.selenium.get("http://" + self.ip + "/~" + self.user + "/WordPress/wp-login.php?action=logout");
            self.selenium.find_element_by_link_text('Logout').click()
            time.sleep(10)
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        return