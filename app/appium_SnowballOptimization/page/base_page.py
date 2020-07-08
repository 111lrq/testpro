import inspect
import json

import allure
import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from app.appium_SnowballOptimization.page.wrapper import handle_black


class BasePage:
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def set_implicitly(self, time):
        self._driver.implicitly_wait(time)

    def screenshot(self, name):
        self._driver.save_screenshot(f"../results/{name}")
        allure.attach.file(f"../results/{name}",attachment_type=allure.attachment_type.PNG)
        # with open(f"../results/{name}","rb") as f:
        #     content=f.read()
        # allure.attach(content,attachment_type=allure.attachment_type.PNG)

    @handle_black
    def finds(self, locator, value: str = None):
        elements: list
        elements = self._driver.find_elements(*locator) if isinstance(locator, tuple) \
            else self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        element = self._driver.find_element(*locator) if isinstance(locator, tuple) \
            else self._driver.find_element(locator, value)
        return element

    # 定位后获取其text属性
    @handle_black
    def find_and_gettext(self, locator, value: str = None):
        element: WebElement
        element_text = self._driver.find_element(*locator).text if isinstance(locator, tuple) \
            else self._driver.find_element(locator, value).text
        return element_text

    def steps(self, path):
        # '../datas/main.yaml'
        # index：0 函数本身 steps；1，一级调用，即调用steps的第一层
        with open(path, encoding="utf-8") as f:
            # 利用栈的深度获取函数名
            name = inspect.stack()[1].function
            steps: list[dict] = yaml.safe_load(f)[name]
        # 序列化，将python的obj数据转化为Json语句，即string格式，以便使用replace对yaml中的公共变量赋值
        raw = json.dumps(steps)
        for key, value in self._params.items():
            # ${name}    | name:12345
            # yaml中的${name}都会替换为12345
            # {key}表变量，或者表示为'${'+key+'}'
            # 转义{{}}={},\\=\
            raw = raw.replace(f'${{{key}}}', value)
        steps = json.loads(raw)
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if action == 'click':
                    self.find(step["by"], step["locator"]).click()
                if action == 'send':
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if action == 'len>0':
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0
