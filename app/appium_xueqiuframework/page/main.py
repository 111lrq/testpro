from selenium.webdriver.common.by import By

from app.appium_xueqiu.page.base_page import BasePage
from app.appium_xueqiu.page.market import Market


class Main(BasePage):
    def goto_market(self):
        # 点击market
        self.find(By.XPATH,'//*[@resource-id="android:id/tabs"]//*[@text="行情"]').click()
        return Market(self._driver)