from web.selenium_wework_register.page.index import Index


class TestRegister():
    def setup(self):
        self.index=Index()

    def test_register(self):
        # self.index.goto_register().register_true()
        self.index.goto_login().goto_register().register_true()
