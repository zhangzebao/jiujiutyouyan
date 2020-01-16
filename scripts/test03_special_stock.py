"""特殊状态股票确认"""
import sys
import os

sys.path.append(os.getcwd())
import pytest
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_log import GetLog

log = GetLog().get_log()


class TestSpecialStock:
    def setup_class(self):
        # 获取PageSpecialStockToast对象
        self.page_special_stock_toast = PageIn.page_get_special_stock_toast()
        # 进入搜索页
        self.page_special_stock_toast.page_click_search_index()

    def teardown_class(self):
        GetDriver.quit_driver()

    def teardown(self):
        self.page_special_stock_toast.page_click_back_btn()

    @pytest.mark.parametrize("code", ["000001", "601577", "603323", "000002"])
    def test01_financial_industry(self, code):
        """特殊行业股票检验"""
        self.page_special_stock_toast.page_check_financial_industry_func(code)
        financial_industry_toast = "金融行业股票，暂不提供财报可信度判断"
        try:
            assert self.page_special_stock_toast.page_get_financial_industry() == financial_industry_toast
        except Exception as e:
            self.page_special_stock_toast.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["002968", "300811", "603489"])
    def test02_check_new_stock(self, code):
        """新上市股票检验"""
        self.page_special_stock_toast.page_check_new_stock_func(code)
        # 综合
        self.page_special_stock_toast.page_click_comprehensive_dial()
        msg = "新上市"
        comprehensive_dial_toast = "新上市股票系统需要根据上市后至少一个完整半年报/年报数据及22个交易日交易数据进行业绩和定价预期确认，再行计算评估结果"
        try:
            assert self.page_special_stock_toast.page_get_comprehensive_dial_toast(msg) == comprehensive_dial_toast
        except Exception as e:
            self.page_special_stock_toast.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code",
                             ["300104", "000939", "000995", "002260", "002604", "300028", "300216", "600074", "600610"])
    def test03_check_stop_to_go_public_stock(self, code):
        """暂停上市股票检验"""
        self.page_special_stock_toast.page_check_new_stock_func(code)
        # 综合
        self.page_special_stock_toast.page_click_comprehensive_dial()
        msg = "暂停上市"
        comprehensive_dial_toast = "由于企业暂停上市，可投度暂停计算"
        try:
            assert self.page_special_stock_toast.page_get_comprehensive_dial_toast(msg) == comprehensive_dial_toast
        except Exception as e:
            self.page_special_stock_toast.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["000003", "600087", "600432"])
    def test04_check_exit_market_stock(self, code):
        """退市股票检查"""
        self.page_special_stock_toast.page_check_new_stock_func(code)
        # 综合
        self.page_special_stock_toast.page_click_comprehensive_dial()
        msg = "已退市"
        comprehensive_dial_toast = "由于企业已退市，可投度停止计算"
        try:
            assert self.page_special_stock_toast.page_get_comprehensive_dial_toast(msg) == comprehensive_dial_toast
        except Exception as e:
            self.page_special_stock_toast.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["000004", "000019", "000031", "000035", "001914"])
    def test05_check_reorganization_stock(self, code):
        """重大资产重组股票检查"""
        self.page_special_stock_toast.page_check_new_stock_func(code)
        # 综合
        self.page_special_stock_toast.page_click_comprehensive_dial()
        msg = "重大资产重组"
        comprehensive_dial_toast = "由于上市公司重大资产重组，系统需要跟踪学习重组后的企业经营业绩一年后输出评估结果"
        try:
            assert self.page_special_stock_toast.page_get_comprehensive_dial_toast(msg) == comprehensive_dial_toast
        except Exception as e:
            self.page_special_stock_toast.base_get_img()
            log.error(e)
            raise

    @pytest.mark.parametrize("code", ["000010", "000409", "000410", "000422"])
    def test06_check_major_risk_stock(self, code):
        """*ST重大经营风险股票检查"""
        self.page_special_stock_toast.page_check_new_stock_func(code)
        # 综合
        self.page_special_stock_toast.page_click_comprehensive_dial()
        msg = "重大经营风险"
        comprehensive_dial_toast = "上市公司存在重大经营风险，审慎起见，暂不提供可投度评估结果"
        try:
            assert self.page_special_stock_toast.page_get_comprehensive_dial_toast(msg) == comprehensive_dial_toast
        except Exception as e:
            self.page_special_stock_toast.base_get_img()
            log.error(e)
            raise

