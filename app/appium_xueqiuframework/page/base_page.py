from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from app.appium_xueqiuframework.page.wrapper import handle_black


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_black
    def finds(self, locator, value: str = None):
        elements:list
        elements = self._driver.find_elements(*locator) if isinstance(locator, tuple) \
            else self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        element = self._driver.find_element(*locator) if isinstance(locator, tuple) \
                else self._driver.find_element(locator, value)
        return element

#     def find_and_gettext(self, locator, value: str = None):
#         element: WebElement
#         try:
#             element_text = self._driver.find_element(*locator).text if isinstance(locator,tuple) \
#                 else self._driver.find_element(locator, value).text
#             # 隐式等待时间恢复
#             self._driver.implicitly_wait(10)
#             # 找到之后 _error_num 归0
#             self._error_num = 0
#             return element_text
#         # 处理黑名单中的弹窗
#         except Exception as e:
#             # 出现异常， 将隐式等待设置小一点，快速的处理弹
#             self._driver.implicitly_wait(1)
#             # 判断异常处理次数
#             if self._error_num > self._max_errnum:
#                 raise e
#             self._error_num += 1
#             # 处理黑名单里面的弹框
#             for ele in self._black_list:
#                 elelist = self._driver.find_and_gettext(*ele)
#                 if len(elelist) > 0:
#                     elelist[0].click()
#                     # 处理完弹框，再将去查找目标元素
#                     return self.find_and_gettext(locator, value)
#                 raise e
