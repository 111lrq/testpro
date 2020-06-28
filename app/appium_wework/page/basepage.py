import logging
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 打印日志
    logging.basicConfig(level=logging.INFO)
    # 弹框 处理的定位列表
    _black_list = [
        (MobileBy.XPATH, '//*[@text="确认"]'),
        (MobileBy.XPATH, "//*[@text='下次再说']"),
        (MobileBy.XPATH, "//*[@text='确定']"),
    ]
    _max_errnum = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value: str = None):
        logging.INFO(locator)
        logging.INFO(value)
        element: WebElement
        try:
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) \
                else self._driver.find_element(locator, value)
            # 隐式等待时间恢复
            self._driver.implicitly_wait(10)
            # 找到之后 _error_num 归0
            self._error_num = 0
            return element
        # 处理黑名单中的弹窗
        except Exception as e:
            # 出现异常， 将隐式等待设置小一点，快速的处理弹
            self._driver.implicitly_wait(1)
            # 判断异常处理次数
            if self._error_num > self._max_errnum:
                raise e
            self._error_num += 1
            # 处理黑名单里面的弹框
            for ele in self._black_list:
                logging.INFO(ele)
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹框，再将去查找目标元素
                    return self.find(locator, value)
                raise e

    def find_and_gettext(self, locator, value: str = None):
        logging.INFO(locator)
        logging.INFO(value)
        element: WebElement
        try:
            element_text = self._driver.find_element(*locator).text if isinstance(locator,tuple) \
                else self._driver.find_element(locator, value).text
            # 隐式等待时间恢复
            self._driver.implicitly_wait(10)
            # 找到之后 _error_num 归0
            self._error_num = 0
            return element_text
        # 处理黑名单中的弹窗
        except Exception as e:
            # 出现异常， 将隐式等待设置小一点，快速的处理弹
            self._driver.implicitly_wait(1)
            # 判断异常处理次数
            if self._error_num > self._max_errnum:
                raise e
            self._error_num += 1
            # 处理黑名单里面的弹框
            for ele in self._black_list:
                elelist = self._driver.find_and_gettext(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹框，再将去查找目标元素
                    return self.find_and_gettext(locator, value)
                raise e
