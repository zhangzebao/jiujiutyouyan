"""特殊行业估值工具结果科目"""
import sys
import os

sys.path.append(os.getcwd())
import pytest
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_log import GetLog

log = GetLog().get_log()


class TestValuationSpecialIndustryResultSubject:
    def setup_class(self):
        # 获取PageValuationSpecialIndustryResultSubject对象
        self.page_valuation_special_industry_subject = PageIn.page_get_valuation_special_industry_result_subject()
        # 进入估值工具
        self.page_valuation_special_industry_subject.page_click_tools()
        self.page_valuation_special_industry_subject.page_click_valuation_tools()

    def teardown_class(self):
        GetDriver.quit_driver()

    def teardown(self):
        self.page_valuation_special_industry_subject.page_click_back_btn()

    @pytest.mark.parametrize("code", ["000001", "601318", "601211"])
    def test01_check_special_industry_result_subject_valuation_pe(self, code):
        """验证特殊行业结果科目1年增速PE-2020估值"""
        self.page_valuation_special_industry_subject.page_special_industry_result_subject_pe_func01(code)
        try:
            assert self.page_valuation_special_industry_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_special_industry_subject.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["000001", "601318", "601211"])
    def test02_check_special_industry_result_subject_valuation_pe(self, code):
        """验证特殊行业结果科目1年增速PE-2021估值"""
        self.page_valuation_special_industry_subject.page_special_industry_result_subject_pe_func02(code)
        try:
            assert self.page_valuation_special_industry_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_special_industry_subject.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["000001", "601318", "601211"])
    def test03_check_special_industry_result_subject_valuation_pe(self, code):
        """验证特殊行业结果科目1年增速PE-2022估值"""
        self.page_valuation_special_industry_subject.page_special_industry_result_subject_pe_func03(code)
        try:
            assert self.page_valuation_special_industry_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_special_industry_subject.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["000001", "601318", "601211"])
    def test04_check_special_industry_result_subject_valuation_pb(self, code):
        """验证特殊行业结果科目2年增速PE-2020估值"""
        self.page_valuation_special_industry_subject.page_special_industry_result_subject_pb_func01(code)
        try:
            assert self.page_valuation_special_industry_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_special_industry_subject.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["000001", "601318", "601211"])
    def test05_check_special_industry_result_subject_valuation_pb(self, code):
        """验证特殊行业结果科目2年增速PE-2021估值"""
        self.page_valuation_special_industry_subject.page_special_industry_result_subject_pb_func02(code)
        try:
            assert self.page_valuation_special_industry_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_special_industry_subject.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["000001", "601318", "601211"])
    def test06_check_special_industry_result_subject_valuation_pb(self, code):
        """验证特殊行业结果科目2年增速PE-2022估值"""
        self.page_valuation_special_industry_subject.page_special_industry_result_subject_pb_func03(code)
        try:
            assert self.page_valuation_special_industry_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_special_industry_subject.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["000001", "601318", "601211"])
    def test07_check_special_industry_result_subject_valuation_ps(self, code):
        """验证特殊行业结果科目3年增速PS-2020估值"""
        self.page_valuation_special_industry_subject.page_special_industry_result_subject_ps_func01(code)
        try:
            assert self.page_valuation_special_industry_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_special_industry_subject.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["000001", "601318", "601211"])
    def test08_check_special_industry_result_subject_valuation_ps(self, code):
        """验证特殊行业结果科目3年增速PS-2021估值"""
        self.page_valuation_special_industry_subject.page_special_industry_result_subject_ps_func02(code)
        try:
            assert self.page_valuation_special_industry_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_special_industry_subject.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["000001", "601318", "601211"])
    def test09_check_special_industry_result_subject_valuation_ps(self, code):
        """验证特殊行业结果科目3年增速PS-2022估值"""
        self.page_valuation_special_industry_subject.page_special_industry_result_subject_ps_func03(code)
        try:
            assert self.page_valuation_special_industry_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_special_industry_subject.base_get_img()
            log.error(e)
            raise

