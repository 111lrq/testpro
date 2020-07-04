from app.appium_xueqiu.page.app import App


class TestSearch:
    def setup(self):
        self.app=App()
        self.search=self.app.start().main().goto_market().goto_search()
    def teardown(self):
        self.app.end()
    def test_search(self):
        self.search.search('alibaba','阿里巴巴')
        assert self.search.is_choose('阿里巴巴')