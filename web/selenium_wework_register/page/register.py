from time import sleep
# from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register():
    def __init__(self,driver:WebDriver):
        self._dirver=driver


    def register_true(self):
        sleep(2)
        self._dirver.find_element_by_id('corp_name').send_keys('hello123')
        self._dirver.find_element_by_id('manager_name').send_keys('hello2222')
        self._dirver.find_element_by_id('register_tel').send_keys('12345678901')
        sleep(5)
        self._dirver.quit()
        return True