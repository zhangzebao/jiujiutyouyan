"""暂停上市、退市、新上市、重大资产重组股票估值工具"""
import sys
import os

sys.path.append(os.getcwd())
import pytest
from time import sleep
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_log import GetLog

log = GetLog().get_log()


class TestValuationOtherStock:
    def setup_class(self):
        # 获取PageValuationOtherStock对象
        self.page_valuation_other_stock = PageIn.page_get_valuation_valuation_other_stock()
        # 进入估值工具
        self.page_valuation_other_stock.page_click_tools()
        self.page_valuation_other_stock.page_click_valuation_tools()

    def teardown_class(self):
        GetDriver.quit_driver()

    @pytest.mark.parametrize("code", ["300104", "000939", "002260"])
    def test01_check_valuation_stop_to_go_public_stock(self, code):
        """检验暂停上市股票估值工具"""
        self.page_valuation_other_stock.page_stop_to_go_public_func(code)
        note = "股票已暂停上市"
        try:
            assert self.page_valuation_other_stock.page_get_important_note() == note
        except Exception as e:
            self.page_valuation_other_stock.base_get_img()
            log.error(e)
            raise
        finally:
            self.page_valuation_other_stock.page_click_important_confirm()

    @pytest.mark.parametrize("code", ["000003", "600087", "600432"])
    def test02_check_valuation_exit_market_stock(self, code):
        """检验退市股票估值工具"""
        self.page_valuation_other_stock.page_exit_market_stock_func(code)
        note = "股票已退市"
        try:
            assert self.page_valuation_other_stock.page_get_important_note() == note
        except Exception as e:
            self.page_valuation_other_stock.base_get_img()
            log.error(e)
            raise
        finally:
            self.page_valuation_other_stock.page_click_important_confirm()

    @pytest.mark.parametrize("code", ["002973", "002968", "603489"])
    def test03_check_valuation_new_stock(self, code):
        """检验新上市股票估值工具"""
        self.page_valuation_other_stock.page_new_stock_func(code)
        note = "新上市股票系统需要上市后至少一个完整年报业绩数据和满22个交易日的交易数据，方能提供具有参考价值的评估结果"
        try:
            assert self.page_valuation_other_stock.page_get_important_note() == note
        except Exception as e:
            self.page_valuation_other_stock.base_get_img()
            log.error(e)
            raise
        finally:
            self.page_valuation_other_stock.page_click_important_confirm()

    @pytest.mark.parametrize("code", ["600988", "001914", "001872"])
    def test04_check_reorganization_stock(self, code):
        """检查重大资产重组股票估值工具"""
        self.page_valuation_other_stock.page_reorganization_stock_func(code)
        note = "股票重大资产重组，请关注并审慎评估重大资产重组所导致的企业主营业务变更及财务数据大幅变动等情况，" \
               "重组后市场对上市公司业绩预期及定价发生的重大变化可能导致工具结果不适用"
        try:
            assert self.page_valuation_other_stock.page_get_important_note() == note
        except Exception as e:
            self.page_valuation_other_stock.base_get_img()
            log.error(e)
            raise
        finally:
            self.page_valuation_other_stock.page_click_important_confirm()
            sleep(1)
            self.page_valuation_other_stock.page_click_back_btn()
