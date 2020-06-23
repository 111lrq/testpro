from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None
    _base_url = ''

    # 类变量在使用方法前赋值
    def __init__(self, driver: WebDriver = None):
        if driver == None:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver
        if self._base_url != '':
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_for_elem(self,conditions,time=10):
        return WebDriverWait(self._driver,time).until(conditions)

    def wait_for_click(self,locator,time=10):
        return WebDriverWait(self._driver,time).until(expected_conditions.element_to_be_clickable(locator))
#       注意element_to_be_clickable方法中是只有一个参数locator，所以此处不可以写成by,locator两个参数，而要写成一个，然后以元组形式传入by,locator两个数据
