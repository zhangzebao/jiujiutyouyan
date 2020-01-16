from time import sleep
import page
from base.base import Base


class PageValuationOtherStock(Base):
    def page_click_tools(self):
        """首页工具"""
        self.base_click(page.tools)

    def page_click_valuation_tools(self):
        """估值工具"""
        self.base_click(page.valuation_tools)

    def page_input_stock_code(self, code):
        """输入股票代码"""
        self.base_input(page.valuation_search, code)

    def page_click_search_btn(self):
        """搜索按钮"""
        self.base_click(page.search_btn)

    def page_click_important_confirm(self):
        """重要提示确定按钮"""
        self.base_click(page.important_confirm)

    def page_click_back_btn(self):
        """返回按钮"""
        self.base_click(page.back_btn)
        sleep(1)

    def page_get_important_note(self):
        """获取重要提示文本"""
        note = self.base_get_text(page.important_note)
        print(note)
        return note

    def page_stop_to_go_public_func(self, code):
        """暂停上市股票组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()

    def page_exit_market_stock_func(self, code):
        """退市股票组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()

    def page_new_stock_func(self, code):
        """新上市股票组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()

    def page_reorganization_stock_func(self, code):
        """重大资产重组股票组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
