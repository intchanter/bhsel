from selenium.webdriver import Firefox

class Config(object):
    def __init__(self, selenium, base_url, brand, timeout = 5):
        self.selenium = selenium
        self.base_url = base_url
        self.timeout = timeout
        self.brand = brand

config = Config(Firefox(), 'http://www.bluehost.com/', 'bluehost')
