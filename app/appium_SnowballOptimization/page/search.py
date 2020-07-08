from app.appium_SnowballOptimization.page.base_page import BasePage


class Search(BasePage):
    # 输入
    def search(self, searchdata):
        # self._driver.save_screenshot("search.png")
        self._params["searchdata"] = searchdata
        self.steps('../datas/search.yaml')
        return self
    # 查询确认
    def search_confirm(self, selectdata):
        # self._driver.save_screenshot("searchconfirm.png")
        self._params["selectdata"] = selectdata
        self.steps('../datas/search.yaml')

    # 加自选
    def add(self, selectdata):
        # self._driver.save_screenshot("add.png")
        self._params["selectdata"] = selectdata
        self.steps('../datas/search.yaml')

    def is_choose(self, selectdata):
        self._params["selectdata"] = selectdata
        return self.steps('../datas/search.yaml')

    # 重置
    def reset(self, selectdata):
        self._params["selectdata"] = selectdata
        return self.steps('../datas/search.yaml')
