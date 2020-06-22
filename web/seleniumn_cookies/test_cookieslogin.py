#标题：使用 cookies 登录企业微信，并点击通讯录
#步骤：(可以分开两个类，一个获取cookie，一个使用，此处写在一个文件中)
#   1.记录cookies (class TestGetCookie)
#   企业微信特点:只要关闭，再打开时就需要重新登录
#   故使用当前网页复用的方式进入网页获取并存储cookies（只适用于仅打开一个浏览器窗口的情况）
#       a.terminal 中开启浏览器 本地选择一个端口用于与chrome（设置其debugging-port）远程通信，
#         chrome --remote-debugging-port=9222
#       本地mac：Google\ Chrome --remote-debugging-port=9222
#       b.py文件中建立login下的setup，teardowm，与操作方法
#       b.setup中实例化options类(chromedriver下)，并将其属性debugger_address赋值(与debugging-port的一致)，确保driver与chrome的通信
#       c.在实例化webdriver chrome时，并将其属性options赋值为实例化的options
#       d.打开浏览器（即使复用当前浏览器窗口也要重新打开一遍来获取cookie数据进行存储）
#       e.定义db为打开shelve小型数据库的cookies文件
#       f.将获取的cookie值存入db的cookie里
#       g.db.close()保存
#   2.使用cookies 登录企业微信(class TestCookieLogin)
#       a.取消复用当前浏览器
#       a.打开浏览器
#       b.打开db的cookie
#       c.对cookie中可能存在小数情况的expire数据做处理
#       d.启用处理后的cookie数据
#       c.再次打开浏览器
#结果：打开企业微信，并且处于登录状态，点击通讯录切换到通讯录的tab
import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.mark.skip
class TestGetCookie():
    def setup_method(self):
        options=Options()
        options.debugger_address="127.0.0.1:9222"
        self.driver=webdriver.Chrome(options=options)
    def teardown_method(self):
        self.driver.quit()
    def test_GetCookie(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db=shelve.open('cookies')
        print(self.driver.get_cookies())
        db['cookie']=self.driver.get_cookies()
        self.driver.find_element_by_class_name("frame_nav_item_title").click()
        db.close()


class TestCookieLogin():
    def setup_method(self):
        self.driver = webdriver.Chrome()
    def teardown_method(self):
        self.driver.quit()
    def test_Cookielogin(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db=shelve.open('cookies')
        cookies=db['cookie']
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_class_name('frame_nav_item_title').click()
        sleep(3)
        # db.close()

#-----------------------------------------------------------------------------------------
#  复用浏览器 课堂
# （仅限当前只打开一个窗口的情况可复用）
#terminal选择一个端口启动打开浏览器 mac：Google\ Chrome --remote-debugging-port:9222(任意端口都可)
#-----------------------------------------------------------------------------------------
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
# class TestDemo():
#     def setup_method(self):
#         options=Options()
#         options.debugger_address='127.0.0.1:9222'
#         self.driver=webdriver.Chrome(options=options)
#     def teardown_method(self):
#         self.driver.quit()
#     def test_demo(self):
#         self.driver.find_element(By.LINK_TEXT,'近期（12）').click()
#         sleep(3)



