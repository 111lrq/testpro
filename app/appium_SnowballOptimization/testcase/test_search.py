import pytest
import yaml

from app.appium_SnowballOptimization.page.app import App


class TestSearch:
    def setup(self):
        self.app = App()
        self.search = self.app.start().main().goto_market().goto_search()

    # def teardown(self):
    #     self.app.end()

    @pytest.mark.parametrize('searchdata,selectdata',yaml.safe_load(open('../datas/test_search.yaml', encoding="utf-8")))
    def test_search(self, searchdata, selectdata):
        self.search.search(searchdata).search_confirm(selectdata)
        if self.search.is_choose(selectdata):
            self.search.reset(selectdata)
        self.search.add(selectdata)
        assert self.search.is_choose(selectdata)

    # def test_search(self):
    #     self.search.search("alibaba").search_confirm("阿里巴巴")
    #     if self.search.is_choose("阿里巴巴"):
    #         self.search.reset("阿里巴巴")
    #     self.search.add("阿里巴巴")
    #     assert self.search.is_choose("阿里巴巴")
