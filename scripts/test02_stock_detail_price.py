"""股票详情估价检查"""
import sys
import os

sys.path.append(os.getcwd())
import pytest
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_log import GetLog

log = GetLog().get_log()


class TestStockDetailPrice:
    def setup_class(self):
        # 获取PageUserCenter对象
        self.page_user_center = PageIn.page_get_user_center()
        # 获取PageStockDetailPrice对象
        self.page_stock_detail_price = PageIn.page_get_stock_detail_price()
        # 进入搜索页
        self.page_stock_detail_price.page_click_search_index()

    def teardown_class(self):
        GetDriver.quit_driver()

    def teardown(self):
        # 返回搜索页
        self.page_stock_detail_price.page_click_back_btn()

    @pytest.mark.parametrize("stock_code", ["000001", "000003", "000004"])
    def test01_check_price(self, stock_code):
        """确认现价"""
        self.page_stock_detail_price.page_get_stock_price_func(stock_code)
        try:
            assert self.page_stock_detail_price.page_get_current_price() != "0.00"
        except Exception as e:
            self.page_stock_detail_price.base_get_img()
            log.error(e)
            raise

