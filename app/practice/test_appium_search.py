from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
改造1： pytest模式
改造2： 改造成可维护的代码形态，绝对不允许有绝对路径的存在 
改造3： 将自动生成的find_element_by_**  改造成find_element(MobileBy.)
改造4： 添加断言 
改造5： 合理使用 setup_class, setup 方法 
"""


class TestXueqiuLu:
    def setup_class(self):
        print('setup_class')
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator-5554"
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        caps['noReset'] = 'true'
        caps['skipServerInstallation'] = True
        caps['skipDeviceInitialization'] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        print('teardown_class')
        self.driver.quit()

    # def setup(self):
    #     print("setup")
    #
    # def teardown(self):
    #     print("teardown")
    #     self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()

    @pytest.mark.parametrize('searchdata,clicktext',[('alibaba','阿里巴巴'),('jd','京东'),('xiaomi','小米集团-W')])
    def test_search(self,searchdata,clicktext):
        # self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_agree").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchdata)
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{clicktext}']").click()
        locator = (MobileBy.ID, "com.xueqiu.android:id/followed_btn")
        WebDriverWait(self.driver,30).until(expected_conditions.element_to_be_clickable(locator))
        ele = self.driver.find_element(*locator)
        print(ele.text)
        if ele.text == '加自选':
            ele.click()
        assert ele.text == '已添加'
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()

        # el4 = self.driver.find_elements(MobileBy.XPATH,
        #                                 f"//*[@text='{clicktext}']/../..//*[@text='加自选']")
        # if len(el4) > 0:
        #     el4[0].click()
        #     self.driver.find_element(MobileBy.XPATH,
        #                              f"//*[@text='{clicktext}']/../..//*[@text='已添加']")
        # else:
        #     print("已加自选")
