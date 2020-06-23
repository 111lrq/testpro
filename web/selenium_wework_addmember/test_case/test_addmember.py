from time import sleep

from web.selenium_wework_addmember.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        add_member= self.main.goto_add_member()
        add_member.add_member('张三999')
        assert add_member.get_member('张三999')
