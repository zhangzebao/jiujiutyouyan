from time import sleep
from base.base import Base
import page


class PageStockDetailPrice(Base):
    def page_click_search_index(self):
        """首页搜索框"""
        self.base_click(page.search_index)

    def page_search_stock_code(self, code):
        """搜索股票代码"""
        self.base_input(page.search_box, code)

    def page_click_search_btn(self):
        """搜索按钮"""
        self.base_click(page.search_btn)

    def page_click_stock_detail(self):
        """进入个股详情"""
        self.base_click(page.stock_detail)

    def page_get_current_price(self):
        """获取现价或收盘价"""
        price = self.base_get_text(page.current_price)
        print(price)
        return str(price)

    def page_click_back_btn(self):
        """返回按钮"""
        self.base_click(page.back_btn)
        sleep(1)

    def page_get_stock_price_func(self, code):
        """获取股票现价或收盘价组合业务方法"""
        self.page_search_stock_code(code)  # 输入股票代码
        sleep(1)
        self.page_click_search_btn()
        self.page_click_stock_detail()
