from time import sleep
from selenium.webdriver.common.by import By

from web.selenium_wework_addmember.page.add_member import AddMember
from web.selenium_wework_addmember.page.base_page import BasePage


class Main(BasePage):
    _base_url = ''

    def goto_add_member(self):
        # self.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        # click通讯录
        self.find(By.ID, 'menu_contacts').click()

        # click 添加成员
        def wait_add_member(x):
            elements_len = len(self.finds(By.CSS_SELECTOR, '#username'))
            if elements_len <= 0:
                self.find(By.CSS_SELECTOR, '.js_add_member:nth-child(2)').click()
            return elements_len > 0

        self.wait_for_elem(wait_add_member)
        # self.find(By.CSS_SELECTOR,'.js_add_member:nth-child(2)').click()
        return AddMember(self._driver)
