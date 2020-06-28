from appium.webdriver.common.mobileby import MobileBy

from app.appium_wework.page.basepage import BasePage
from app.appium_wework.page.member_invite import MemberInvite


class AddressList(BasePage):
    def addmember(self):
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h9u").click()
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return MemberInvite(self._driver)
