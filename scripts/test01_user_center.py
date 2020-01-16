"""个人中心"""
import sys
import os

sys.path.append(os.getcwd())
import pytest
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_log import GetLog

log = GetLog().get_log()


class TestUserCenter:
    def setup_class(self):
        # 获取PageUserCenter对象
        self.page_user_center = PageIn.page_get_user_center()
        # 进入个人中心
        self.page_user_center.page_into_user_center_func()

    def teardown_class(self):
        GetDriver.quit_driver()

    @pytest.mark.parametrize("nickname", ["000001", "000002", "000003"])
    def test01_modify_nickname(self, nickname):
        self.page_user_center.page_modify_nickname_func(nickname)
        try:
            assert self.page_user_center.page_get_nickname_text() == nickname
        except Exception as e:
            self.page_user_center.base_get_img()
            log.error(e)
            raise

    def test02_modify_sex(self):
        self.page_user_center.page_modify_sex_func()
        try:
            assert self.page_user_center.page_get_sex_text() == "男"
        except Exception as e:
            self.page_user_center.base_get_img()
            log.error(e)
            raise

    def test03_modify_profession(self, profession="软件测试"):
        self.page_user_center.page_modify_profession_func(profession)
        try:
            assert self.page_user_center.page_get_profession_text() == profession
        except Exception as e:
            self.page_user_center.base_get_img()
            log.error(e)
            raise

    def test04_modify_mailing_address(self, address="北京市朝阳区"):
        self.page_user_center.page_modify_mailing_address_func(address)
        try:
            assert self.page_user_center.page_get_mailing_address_text() == address
        except Exception as e:
            self.page_user_center.base_get_img()
            log.error(e)
            raise

    def test05_modify_email(self, email="13155481641@163.com"):
        self.page_user_center.page_modify_email_func(email)
        try:
            assert self.page_user_center.page_get_email_text() == email
        except Exception as e:
            self.page_user_center.base_get_img()
            log.error(e)
            raise

    def test06_modify_introduction(self, introduction="你,就是大师!YOU ARE MASTER"):
        self.page_user_center.page_modify_introduction_func(introduction)
        try:
            assert self.page_user_center.page_get_introduction_text() == introduction
        except Exception as e:
            self.page_user_center.base_get_img()
            log.error(e)
            raise
