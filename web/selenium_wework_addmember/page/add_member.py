from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.selenium_wework_addmember.page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self,name):
        self.find(By.ID, 'username').send_keys(name)
        self.find(By.ID, 'memberAdd_acctid').send_keys('abcdddd')
        self.find(By.ID, 'memberAdd_phone').send_keys('12345678901')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def update_page(self):
        content:str=self.find(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
        return [int(x) for x in content.split('/',1)]

    def get_member(self,name):
        # self.wait_for_click(By.CSS_SELECTOR,".ww_checkbox")
        self.wait_for_click((By.CSS_SELECTOR, ".ww_checkbox"))
        cur_page,total_page= self.update_page()
        while True:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            list = [element.get_attribute("title") for element in elements]
            if name in list:
                return True
            cur_page=self.update_page()[0]
            if cur_page==total_page:
                return False
            self.find(By.CSS_SELECTOR,'.ww_commonImg_PageNavArrowRightNormal').click()

