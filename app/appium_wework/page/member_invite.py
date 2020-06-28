from appium.webdriver.common.mobileby import MobileBy

from app.appium_wework.page.basepage import BasePage


class MemberInvite(BasePage):
    def addmember_manul(self):
        from app.appium_wework.page.contact_add import ContactAdd
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return ContactAdd(self._driver)

    def get_toast(self):
        return self.find_and_gettext(MobileBy.XPATH, "//*[@class= 'android.widget.Toast']")
