from selenium.webdriver.common.by import By

from app.appium_xueqiuframework.page.base_page import BasePage
from app.appium_xueqiuframework.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # 点击research.模拟弹窗等黑名单的情况
        # self.find(By.XPATH,'//*[contains(@resource-id,"action_search"]').click()
        # self.find(By.ID, 'com.xueqiu.android:id/action_search').click()
        return Search(self._driver)