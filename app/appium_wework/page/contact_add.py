from appium.webdriver.common.mobileby import MobileBy

from app.appium_wework.page.basepage import BasePage


class ContactAdd(BasePage):

    def input_name(self):
        name_ele = "//*[@text='姓名'/../*[@class='android.widget.EditText']]"
        # self.driver.find(MobileBy.XPATH, name_ele).send_keys('name')
        self.find(MobileBy.XPATH, name_ele).send_keys('Name1')
        return self

    def set_gender(self):
        gender_ele = "//*[@text=性别'/../*[contains(@class,'ImageView')]]"  # "//*[@text='性别']/..//*[contains(@class, 'TextView') and @text='男']"
        self.find(MobileBy.XPATH, gender_ele).click()
        # self.driver.find(MobileBy.XPATH, f"//*[@text='{gender}']").click()
        self.find(MobileBy.XPATH, f"//*[@text='女']").click()
        return self

    def input_phonenum(self):
        phone_ele = "//*[@text=手机'/../*[contains(@class,'EditText')]]"
        # self.driver.find(MobileBy.XPATH, phone_ele).send_keys(phone)
        self.find(MobileBy.XPATH, phone_ele).send_keys('12345678900')
        return self

    def click_save(self):
        from app.appium_wework.page.member_invite import MemberInvite
        return MemberInvite(self._driver)
