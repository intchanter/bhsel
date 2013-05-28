import time
class PhpConf():
    def __init__(self, selenium):
        self.selenium = selenium
    def phpv(self, phpver):
        phparg = {'52' : 'php5', '52s':'php5s', '52f':'php5cgi', '53':'php53', '53s':'php53s', '54':'php54', '54s':'php54s'}
        phpv = phparg[phpver]
        handles = self.selenium.window_handles
        self.selenium.switch_to_window(handles[1])
        self.selenium.find_element_by_id('item_php-config').click()
        time.sleep(10)
        self.selenium.find_element_by_css_selector("input[value="+phpv+"]").click()
        self.selenium.find_element_by_css_selector('input[value="SAVE CHANGES"]').click()
        time.sleep(10)
        self.selenium.find_element_by_link_text('cPanel').click()
        return
    