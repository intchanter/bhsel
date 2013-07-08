import time
from selenium.webdriver.common.keys import Keys
from simplescripts import SS
from selenium import webdriver

class MWTest():
    def __init__(self, selenium, path, etime, ip, user, dom, isbeta):
        self.selenium = selenium
        self.path = path
        self.etime = time
        self.ip = ip
        self.user = user
        self.domain = dom
        self.isbeta = isbeta
        
    def mediawiki(self, phpv):
        if (self.isbeta == 0):
            #chains = webdriver.ActionChains(self.selenium)
            #chains.key_down(Keys.COMMAND)
            self.selenium.find_element_by_id('item_simplescripts-sb').click() #send_keys(Keys.CONTROL + "N")
            #chains.key_up(Keys.COMMAND)
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://www." +self.domain+ "/MediaWiki/index.php?title=Main_Page")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('site-info')):
                print('Wordpress not installed to /WordPress Directory installing')
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('MediaWiki', 5, self.domain)
                self.selenium.get("http://www." +self.domain+ "/MediaWiki/index.php?title=Main_Page")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + 'mw1-' + phpv + '.png')
            self.selenium.get("http://www."+self.domain+"/MediaWiki/index.php?title=Special:UserLogin")
            time.sleep(10)
            self.selenium.save_screenshot(self.path + "mw2-" + phpv + ".png")
            self.selenium.find_element_by_name('wpName').clear()
            self.selenium.find_element_by_name('wpName').send_keys('seleniumhumantwo@bluehost.com')
            self.selenium.find_element_by_name('wpPassword').clear()
            self.selenium.find_element_by_name('wpPassword').send_keys('Test1234')
            self.selenium.find_element_by_id('wpLoginAttempt').click()
            self.selenium.save_screenshot(self.path + "mw3-" + phpv + ".png")
            time.sleep(10)
            if (self.selenium.find_elements_by_link_text('Log out')):
                #self.selenium.save_screenshot(self.path + "mw3-" + phpv + ".png")
                #self.selenium.get("http://www." + self.domain + "/WordPress/wp-login.php?action=logout")
                self.selenium.find_element_by_link_text('Log out').click()
            else:
                self.selenium.get('http://www." +self.domain+ "/MediaWiki/index.php?title=Main_Page')
                time.sleep(3)
                self.selenium.find_element_by_link_text('Log out').click()
            time.sleep(10)
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/MediaWiki/index.php?title=Main_Page")
            self.selenium.save_screenshot(self.path + "mw4" + phpv + ".png")
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        else:
            self.selenium.find_element_by_id('item_simplescripts-sb').click()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[2])
            self.selenium.get("http://" + self.ip + "/~" + self.user + "/MediaWiki/index.php?title=Main_Page")
            time.sleep(5)
            if not (self.selenium.find_elements_by_class_name('site-info')):
                self.selenium.close()
                handles = self.selenium.window_handles
                self.selenium.switch_to_window(handles[1])
                simple = SS(self.selenium)
                simple.get_to_simplescripts()
                simple.install_script('MediaWiki', 5, self.domain)
                self.selenium.get("http://" + self.ip +"/~" + self.user + "/MediaWiki/index.php?title=Main_Page")
                time.sleep(5)
            self.selenium.save_screenshot(self.path + "mw1" + phpv + ".png")
            self.selenium.get("http://"+self.ip+"/~"+self.user+"/MediaWiki/index.php?title=Special:UserLogin")
            self.selenium.save_screenshot(self.path + "mw2" + phpv + ".png")
            self.selenium.find_element_by_name('log').clear()
            self.selenium.find_element_by_name('log').send_keys('admin')
            self.selenium.find_element_by_name('pwd').clear()
            self.selenium.find_element_by_name('pwd').send_keys('Test1234')
            self.selenium.find_element_by_name('wp-submit').click()
            self.selenium.save_screenshot(self.path + "mw3" + phpv + ".png")
            #(self.selenium.get("http://" + self.ip + "/~" + self.user + "/WordPress/wp-login.php?action=logout");
            if (self.selenium.find_elements_by_link_text('Log out')):
                self.selenium.find_element_by_link_text('Log out').click()
            else:
                self.selenium.get("http://" + self.ip +"/~" + self.user + "/MediaWiki/index.php?title=Main_Page")
                time.sleep(3)
                self.selenium.find_element_by_link_text('Log out').click()
            time.sleep(10)
            self.selenium.close()
            handles = self.selenium.window_handles
            self.selenium.switch_to_window(handles[1])
        return