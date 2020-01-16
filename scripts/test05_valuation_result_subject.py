"""非特殊股票估值工具结果科目"""
import sys
import os

sys.path.append(os.getcwd())
from tool.read_text import read_text
import pytest
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_log import GetLog

log = GetLog().get_log()


def get_data():
    data_list = []
    for code in read_text("code"):
        code = code.strip('\n')
        data_list.append(code)
    return data_list


class TestValuationResultSubject:
    def setup_class(self):
        # 获取PageValuationResultSubject对象
        self.page_valuation_result_subject = PageIn.page_get_valuation_result_subject()
        # 进入估值工具页
        self.page_valuation_result_subject.page_click_tools()
        self.page_valuation_result_subject.page_click_valuation_tools()

    def teardown_class(self):
        GetDriver.quit_driver()

    def teardown(self):
        self.page_valuation_result_subject.page_click_back_btn()

    @pytest.mark.parametrize("code", get_data())
    def test01_check_result_subject_valuation_pe(self, code):
        """验证结果科目1年增速PE-2020估值"""
        self.page_valuation_result_subject.page_result_subject_pe_func01(code)
        try:
            assert self.page_valuation_result_subject.page_get_valuation_result() > 0.00
            assert self.page_valuation_result_subject.page_get_valuation_result() < 2000
        except Exception as e:
            self.page_valuation_result_subject.base_get_img()
            print("异常估值股票代码:", code)
            log.error(e)
            raise
        finally:
            print(self.page_valuation_result_subject.page_get_valuation_result())

    @pytest.mark.parametrize("code", get_data())
    def test02_check_result_subject_valuation_pe(self, code):
        """验证结果科目2年增速PE-2020估值"""
        self.page_valuation_result_subject.page_result_subject_pe_func02(code)
        try:
            assert self.page_valuation_result_subject.page_get_valuation_result() > 0.00
            assert self.page_valuation_result_subject.page_get_valuation_result() < 2000
        except Exception as e:
            self.page_valuation_result_subject.base_get_img()
            print("异常估值股票代码:", code)
            log.error(e)
            raise
        finally:
            print(self.page_valuation_result_subject.page_get_valuation_result())

    @pytest.mark.parametrize("code", get_data())
    def test03_check_result_subject_valuation_pe(self, code):
        """验证结果科目3年增速PE-2020估值"""
        self.page_valuation_result_subject.page_result_subject_pe_func03(code)
        try:
            assert self.page_valuation_result_subject.page_get_valuation_result() > 0.00
            assert self.page_valuation_result_subject.page_get_valuation_result() < 2000
        except Exception as e:
            self.page_valuation_result_subject.base_get_img()
            print("异常估值股票代码:", code)
            log.error(e)
            raise
        finally:
            print(self.page_valuation_result_subject.page_get_valuation_result())

    @pytest.mark.parametrize("code", ["000002", "000029", "000599"])
    def test04_check_result_subject_valuation_pe(self, code):
        """验证结果科目1年增速PE-2021估值"""
        self.page_valuation_result_subject.page_result_subject_pe_func04(code)
        try:
            assert self.page_valuation_result_subject.page_get_valuation_result() > 0.00
            assert self.page_valuation_result_subject.page_get_valuation_result() < 2000
        except Exception as e:
            self.page_valuation_result_subject.base_get_img()
            log.error(e)
            raise
        finally:
            print(self.page_valuation_result_subject.page_get_valuation_result())
            if self.page_valuation_result_subject.page_get_valuation_result() > 2000:
                print(code)

    # @pytest.mark.parametrize("code", ["000002", "002072", "000005"])
    # def test05_check_result_subject_valuation_pe(self, code):
    #     """验证结果科目2年增速PE-2021估值"""
    #     self.page_valuation_result_subject.page_result_subject_pe_func05(code)
    #     try:
    #         assert self.page_valuation_result_subject.page_get_valuation_result() > "0.00"
    #     except Exception as e:
    #         self.page_valuation_result_subject.base_get_img()
    #         log.error(e)
    #         raise
    #
    # @pytest.mark.parametrize("code", ["000002", "002072", "000005"])
    # def test06_check_result_subject_valuation_pe(self, code):
    #     """验证结果科目3年增速PE-2021估值"""
    #     self.page_valuation_result_subject.page_result_subject_pe_func06(code)
    #     try:
    #         assert self.page_valuation_result_subject.page_get_valuation_result() > "0.00"
    #     except Exception as e:
    #         self.page_valuation_result_subject.base_get_img()
    #         log.error(e)
    #         raise

    @pytest.mark.parametrize("code", ["000002", "002072", "000005"])
    def test07_check_result_subject_valuation_pe(self, code):
        """验证结果科目1年增速PE-2022估值"""
        self.page_valuation_result_subject.page_result_subject_pe_func07(code)
        try:
            assert self.page_valuation_result_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_result_subject.base_get_img()
            log.error(e)
            raise

    # @pytest.mark.parametrize("code", ["000002", "002072", "000005"])
    # def test08_check_result_subject_valuation_pe(self, code):
    #     """验证结果科目2年增速PE-2022估值"""
    #     self.page_valuation_result_subject.page_result_subject_pe_func08(code)
    #     try:
    #         assert self.page_valuation_result_subject.page_get_valuation_result() > "0.00"
    #     except Exception as e:
    #         self.page_valuation_result_subject.base_get_img()
    #         log.error(e)
    #         raise
    #
    # @pytest.mark.parametrize("code", ["000002", "002072", "000005"])
    # def test09_check_result_subject_valuation_pe(self, code):
    #     """验证结果科目3年增速PE-2022估值"""
    #     self.page_valuation_result_subject.page_result_subject_pe_func09(code)
    #     try:
    #         assert self.page_valuation_result_subject.page_get_valuation_result() > "0.00"
    #     except Exception as e:
    #         self.page_valuation_result_subject.base_get_img()
    #         log.error(e)
    #         raise

    @pytest.mark.parametrize("code", get_data())
    def test10_check_result_subject_valuation_pb(self, code):
        """验证结果科目2年增速PB-2020估值"""
        self.page_valuation_result_subject.page_result_subject_pb_func01(code)
        try:
            assert self.page_valuation_result_subject.page_get_valuation_result() > 0.00
            assert self.page_valuation_result_subject.page_get_valuation_result() < 2000
        except Exception as e:
            self.page_valuation_result_subject.base_get_img()
            print("异常估值股票代码:", code)
            log.error(e)
            raise
        finally:
            print(self.page_valuation_result_subject.page_get_valuation_result())

    @pytest.mark.parametrize("code", ["000002", "002072", "000005"])
    def test11_check_result_subject_valuation_pb(self, code):
        """验证结果科目2年增速PB-2021估值"""
        self.page_valuation_result_subject.page_result_subject_pb_func02(code)
        try:
            assert self.page_valuation_result_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_result_subject.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["000002", "002072", "000005"])
    def test12_check_result_subject_valuation_pb(self, code):
        """验证结果科目2年增速PB-2022估值"""
        self.page_valuation_result_subject.page_result_subject_pb_func03(code)
        try:
            assert self.page_valuation_result_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_result_subject.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", get_data())
    def test13_check_result_subject_valuation_ps(self, code):
        """验证结果科目3年增速PS-2020估值"""
        self.page_valuation_result_subject.page_result_subject_ps_func01(code)
        try:
            assert self.page_valuation_result_subject.page_get_valuation_result() > 0.00
            assert self.page_valuation_result_subject.page_get_valuation_result() < 2000
        except Exception as e:
            self.page_valuation_result_subject.base_get_img()
            print("异常估值股票代码:", code)
            log.error(e)
            raise
        finally:
            print(self.page_valuation_result_subject.page_get_valuation_result())

    @pytest.mark.parametrize("code", ["000002", "002072", "000005"])
    def test14_check_result_subject_valuation_ps(self, code):
        """验证结果科目3年增速PS-2021估值"""
        self.page_valuation_result_subject.page_result_subject_ps_func02(code)
        try:
            assert self.page_valuation_result_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_result_subject.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["000002", "002072", "000005"])
    def test15_check_result_subject_valuation_ps(self, code):
        """验证结果科目3年增速PS-2022估值"""
        self.page_valuation_result_subject.page_result_subject_ps_func03(code)
        try:
            assert self.page_valuation_result_subject.page_get_valuation_result() > "0.00"
        except Exception as e:
            self.page_valuation_result_subject.base_get_img()
            log.error(e)
            raise
