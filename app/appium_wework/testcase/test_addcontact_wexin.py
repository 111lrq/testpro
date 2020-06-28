from app.appium_wework.page.app import App
from app.appium_wework.page.member_invite import MemberInvite


class TestContact:
    def setup(self):
        self.app=App()
        self.main=self.app.start().main()

    def test_addcontact(self):
        invite=self.main.goto_addresslist().addmember().addmember_manul().\
            input_name().set_gender().input_phonenum().click_save()
        assert "添加成功" in invite.get_toast()


     # def  test_addcontact(self):
     #    invitpage = self.main.goto_addresslist().add_member(). \
     #        addmember_by_manul().input_name().set_gender() \
     #        .input_phonenum().click_save()
     #
     #    # assert '成功' in invitpage.get_toast()