import yaml
from selenium.webdriver.common.by import By

from app.appium_SnowballOptimization.page.base_page import BasePage
from app.appium_SnowballOptimization.page.market import Market


class Main(BasePage):
    def goto_market(self):
        # 点击market
        # self.set_implicitly(10)
        self.steps("../datas/main.yaml")
        # self.set_implicitly(3)
        return Market(self._driver)