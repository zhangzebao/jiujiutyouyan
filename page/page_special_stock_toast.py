from time import sleep
import page
from base.base import Base


class PageSpecialStockToast(Base):
    def page_click_search_index(self):
        """首页搜索框"""
        self.base_click(page.search_index)

    def page_search_stock_code(self, code):
        """搜索股票代码"""
        self.base_input(page.search_box, code)

    def page_click_search_btn(self):
        """搜索按钮"""
        self.base_click(page.search_btn)

    def page_click_back_btn(self):
        """返回按钮"""
        self.base_click(page.back_btn)
        sleep(1)

    def page_click_comprehensive_dial(self):
        """综合表盘"""
        self.base_click(page.Comprehensive_dial)

    def page_get_comprehensive_dial_toast(self, msg):
        """获取综合表盘toast"""
        toast = self.base_get_toast("{}".format(msg))
        print(toast)
        return toast

    def page_click_base_face_dial(self):
        """基本面表盘"""
        self.base_click(page.Base_face_dial)

    # def page_get_base_face_dial_toast(self, msg):
    #     """获取基本面表盘toast"""
    #     toast = self.base_get_toast("{}".format(msg))
    #     print(toast)
    #     return toast

    def page_click_report_reliable_dial(self):
        """财报可信度"""
        self.base_click(page.Report_reliable_dial)

    # def page_get_report_reliable_dial(self, msg):
    #     """获取财报可信度toast"""
    #     toast = self.base_get_toast("{}".format(msg))
    #     print(toast)
    #     return toast

    def page_click_now_the_rate_dial(self):
        """估现差率"""
        self.base_click(page.Now_the_rate_dial)

    # def page_get_now_the_rate_dial_toast(self, msg):
    #     """获取估现差率toast"""
    #     toast = self.base_get_toast("{}".format(msg))
    #     print(toast)
    #     return toast

    def page_click_fluctuation_risk_dial(self):
        """波动风险"""
        self.base_click(page.Fluctuation_risk_dial)

    # def page_get_fluctuation_risk_dial_toast(self, msg):
    #     """获取波动风险toast"""
    #     toast = self.base_get_toast("{}".format(msg))
    #     print(toast)
    #     return toast

    def page_get_financial_industry(self):
        """获取金融行业toast"""
        toast = self.base_get_toast("金融行业股票")
        print(toast)
        return toast

    def page_check_financial_industry_func(self, code):
        """验证金融行业toast组合业务方法"""
        self.page_search_stock_code(code)
        sleep(1)
        self.page_click_search_btn()

    def page_check_new_stock_func(self, code):
        """验证新股toast组合业务方法"""
        self.page_search_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_comprehensive_dial()
        sleep(1)
