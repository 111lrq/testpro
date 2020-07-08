from selenium.webdriver.common.by import By

from app.appium_SnowballOptimization.page.base_page import BasePage
from app.appium_SnowballOptimization.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # 点击research
        # self.steps('../datas/market.yaml')
        return Search(self._driver)

    # goto_search:
    # -by: id
    # locator: 'com.xueqiu.android:id/action_search'
    # action: click