import pytest
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy

from app.appium_xueqiu.page.base_page import BasePage


class Search(BasePage):
    # @pytest.mark.parametrize('searchdata,clicktext', [('阿里巴巴', 'BABA')])
    def search(self, searchdata, clicktext):
        # 输入
        self.find(MobileBy.XPATH, '//*[contains(@resource-id,"search_input_text")]').send_keys(searchdata)
        # 查询

        self.find(MobileBy.XPATH, f'//*[@text="{clicktext}"]/..').click()
        # 加自选
        ele = self.finds(MobileBy.XPATH, f'//*[@text="{clicktext}"]/../..//*[@text="加自选"]')
        if len(ele) > 0:
            # WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
            ele[0].click()

    # @pytest.mark.parametrize('data',['BABA'])
    def is_choose(self, clicktext):
        eles: WebElement = self.finds(MobileBy.XPATH, f'//*[@text="{clicktext}"]/../..//*[@text="已添加"]')
        return len(eles) > 0

   # def is_choose(self, value):
   #      element: WebElement = self.find(MobileBy.XPATH, f"//*[@text='{value}']/../../..//*[@text='已添加']")
   #      return True if element else False