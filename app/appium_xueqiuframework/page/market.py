from selenium.webdriver.common.by import By

from app.appium_xueqiu.page.base_page import BasePage
from app.appium_xueqiu.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # 点击research
        # self.find(By.XPATH,'//*[contains(@resource-id,"action_search"]').click()
        self.find(By.ID, 'com.xueqiu.android:id/action_search').click()
        return Search(self._driver)