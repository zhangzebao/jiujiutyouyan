from time import sleep
from base.base import Base
import page


class PageUserCenter(Base):
    def page_click_disclaimer(self):
        """免责声明"""
        self.base_click(page.disclaimer)

    def page_click_my(self):
        """我的"""
        self.base_click(page.my)

    def page_click_close_optional(self):
        """推荐自选"""
        self.base_click(page.close_optional)

    def page_click_personal_center(self):
        """个人中心"""
        self.base_click(page.personal_center)

    def page_click_to_login(self):
        """去登录"""
        self.base_click(page.to_login)

    def page_input_phone(self, phone):
        """手机号码"""
        self.base_input(page.input_phone, phone)

    def page_input_img_code(self):
        """图片验证码"""
        img_code = input("请输入图片验证码:")
        print("图片验证码为:", img_code)
        self.base_input(page.input_img_code, img_code)

    def page_input_note_code(self, note_code):
        """短信验证码"""
        self.base_input(page.input_note_code, note_code)

    def page_click_login_btn(self):
        """登录"""
        self.base_click(page.login_btn)

    def page_click_software_setting(self):
        """软件设置"""
        self.base_click(page.software_setting)

    def page_click_personal_information(self):
        """个人信息"""
        self.base_click(page.personal_information)

    def page_click_nickname(self):
        """昵称"""
        self.base_click(page.nickname)

    def page_input_nickname(self, nickname):
        """编辑昵称"""
        self.base_input(page.edit_nickname, nickname)

    def page_click_confirm_btn(self):
        """确定按钮"""
        self.base_click(page.confirm_btn)

    def page_click_sex(self):
        """性别"""
        self.base_click(page.Sex)

    def page_sex_selection(self):
        """选择性别"""
        self.base_click(page.sex_selection)

    def page_click_profession(self):
        """职业"""
        self.base_click(page.profession)

    def page_input_profession(self, profession):
        """输入职业"""
        self.base_input(page.input_profession, profession)

    def page_click_mailing_address(self):
        """通信地址"""
        self.base_click(page.mailing_address)

    def page_input_address(self, address):
        """输入通信地址"""
        self.base_input(page.input_address, address)

    def page_click_email(self):
        """邮箱"""
        self.base_click(page.email)

    def page_input_email(self, email):
        """输入邮箱"""
        self.base_input(page.input_email, email)

    def page_click_introduction(self):
        """个性签名"""
        self.base_click(page.introduction)

    def page_input_introduction(self, introduction):
        """输入个人简介"""
        self.base_input(page.input_introduction, introduction)

    def page_click_confirm_personal(self):
        """个人简介确定按钮"""
        self.base_click(page.confirm_personal)

    def page_click_personal_center_back_btn(self):
        """返回按钮"""
        self.base_click(page.personal_center_back_btn)

    def page_get_nickname_text(self):
        """获取昵称"""
        print(self.base_get_text(page.verify_nickname))
        return self.base_get_text(page.verify_nickname)

    def page_get_sex_text(self):
        """获取性别"""
        print(self.base_get_text(page.verify_sex))
        return self.base_get_text(page.verify_sex)

    def page_get_profession_text(self):
        """获取职业"""
        print(self.base_get_text(page.verify_profession))
        return self.base_get_text(page.verify_profession)

    def page_get_mailing_address_text(self):
        """获取通信地址"""
        print(self.base_get_text(page.verify_mailing_address))
        return self.base_get_text(page.verify_mailing_address)

    def page_get_email_text(self):
        """获取邮箱"""
        print(self.base_get_text(page.verify_email))
        return self.base_get_text(page.verify_email)

    def page_get_introduction_text(self):
        """获取个性签名"""
        print(self.base_get_text(page.verify_introduction))
        return self.base_get_text(page.verify_introduction)

    # 有固定的图片验证码启用
    # def page_login_func(self, phone="13366666666", note_code="160606"):
    #     """登录组合业务方法"""
    #     sleep(2)
    #     self.page_click_disclaimer()
    #     self.page_click_my()
    #     self.page_click_close_optional()
    #     self.page_click_personal_center()
    #     sleep(2)
    #     self.page_click_to_login()
    #     sleep(2)
    #     self.page_input_phone(phone)
    #     # self.page_input_img_code()
    #     sleep(20)
    #     self.page_input_note_code(note_code)
    #     self.page_click_login_btn()
    #     self.page_click_disclaimer()

    def page_into_user_center_func(self):
        """进入个人中心组合业务方法"""
        self.page_click_my()
        self.page_click_personal_center()
        sleep(1)
        self.page_click_software_setting()
        sleep(1)
        self.page_click_personal_information()

    def page_modify_nickname_func(self, nickname):
        """更改昵称组合业务方法"""
        sleep(1)
        self.page_click_nickname()
        self.page_input_nickname(nickname)
        self.page_click_confirm_btn()
        sleep(1)
        self.page_click_personal_center_back_btn()
        sleep(1)
        self.page_click_personal_center_back_btn()
        self.page_get_nickname_text()
        sleep(1)
        self.page_click_software_setting()  # 软件设置
        sleep(1)
        self.page_click_personal_information()  # 个人中心

    def page_modify_sex_func(self):
        """更改性别组合业务方法"""
        sleep(2)
        self.page_click_sex()
        self.page_sex_selection()
        self.page_get_sex_text()

    def page_modify_profession_func(self, profession):
        """更改职业组合业务方法"""
        sleep(2)
        self.page_click_profession()
        self.page_input_profession(profession)
        self.page_click_confirm_btn()
        self.page_get_profession_text()

    def page_modify_mailing_address_func(self, address):
        """更改通信地址组合业务方法"""
        sleep(2)
        self.page_click_mailing_address()
        self.page_input_address(address)
        self.page_click_confirm_btn()
        self.page_get_mailing_address_text()

    def page_modify_email_func(self, email):
        """更改邮箱组合业务方法"""
        sleep(2)
        self.page_click_email()
        self.page_input_email(email)
        self.page_click_confirm_btn()
        self.page_get_email_text()

    def page_modify_introduction_func(self, introduction):
        """更改个性签名组合业务方法"""
        sleep(2)
        self.page_click_introduction()
        self.page_input_introduction(introduction)
        self.page_click_confirm_personal()
        self.page_get_introduction_text()


if __name__ == '__main__':
    # PageUserCenter().page_login_func()
    sleep(2)
    PageUserCenter().page_modify_nickname_func(nickname="软件测试工程师")
    sleep(2)
    PageUserCenter().page_modify_sex_func()
    sleep(2)
    PageUserCenter().page_modify_profession_func(profession="Java开发工程师")
    sleep(2)
    PageUserCenter().page_modify_mailing_address_func("北京朝阳")
    sleep(2)
    PageUserCenter().page_modify_email_func("13325644754@163.com")
    sleep(2)
    PageUserCenter().page_modify_introduction_func("金融分析师,在干嘛呢?")
