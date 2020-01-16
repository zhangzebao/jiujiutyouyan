from time import sleep
import page
from base.base import Base


class PageValuationTools(Base):
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

    def page_click_select_growth_rate(self):
        """选择增速按钮"""
        self.base_click(page.select_growth_rate)

    def page_click_one_year_growth_rate(self):
        """最近1年增速"""
        self.base_click(page.one_year_growth_rate)

    def page_click_two_year_growth_rate(self):
        """最近2年增速"""
        self.base_click(page.two_year_growth_rate)

    def page_click_three_year_growth_rate(self):
        """最近3年增速"""
        self.base_click(page.three_year_growth_rate)

    def page_click_back_btn(self):
        """返回按钮"""
        self.base_click(page.back_btn)
        sleep(1)

    def page_click_select_date(self):
        """选择日期"""
        self.base_click(page.year2020)

    def page_click_date2021(self):
        """2021"""
        self.base_click(page.year2021)

    def page_click_date2022(self):
        """2022"""
        self.base_click(page.year2022)

    def page_click_valuation_pb(self):
        """pb估值"""
        self.base_click(page.valuation_pb)

    def page_click_valuation_pe(self):
        """pe估值"""
        self.base_click(page.valuation_pe)

    def page_click_valuation_ps(self):
        """ps估值"""
        self.base_click(page.valuation_ps)

    def page_get_valuation_result(self):
        """获取我的估值结果"""
        result = self.base_get_text(page.valuation_result)
        return float(result)

    def page_valuation_tools_pb_func01(self, code):
        """估值工具1年增速PB-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_one_year_growth_rate()
        sleep(1)

    def page_valuation_tools_pb_func02(self, code):
        """估值工具2年增速PB-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()
        sleep(1)

    def page_valuation_tools_pb_func03(self, code):
        """估值工具3年增速PB-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()
        sleep(1)

    def page_valuation_tools_pb_func04(self, code):
        """估值工具1年增速PB-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_one_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_valuation_tools_pb_func05(self, code):
        """估值工具2年增速PB-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_valuation_tools_pb_func06(self, code):
        """估值工具3年增速PB-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_valuation_tools_pb_func07(self, code):
        """估值工具1年增速PB-2022估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_one_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()

    def page_valuation_tools_pb_func08(self, code):
        """估值工具2年增速PB-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()

    def page_valuation_tools_pb_func09(self, code):
        """估值工具3年增速PB-2022估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()

    def page_valuation_tools_pe_func01(self, code):
        """估值工具1年增速PE-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_one_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_pe()

    def page_valuation_tools_pe_func02(self, code):
        """估值工具2年增速PE-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_pe()

    def page_valuation_tools_pe_func03(self, code):
        """估值工具3年增速PE-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_pe()

    def page_valuation_tools_pe_func04(self, code):
        """估值工具1年增速PE-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_one_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_pe()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_valuation_tools_pe_func05(self, code):
        """估值工具2年增速PE-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_pe()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_valuation_tools_pe_func06(self, code):
        """估值工具3年增速PE-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_pe()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_valuation_tools_pe_func07(self, code):
        """估值工具1年增速PE-2022估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_one_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_pe()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()

    def page_valuation_tools_pe_func08(self, code):
        """估值工具2年增速PE-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_pe()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()

    def page_valuation_tools_pe_func09(self, code):
        """估值工具3年增速PE-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_pe()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()

    def page_valuation_tools_ps_func01(self, code):
        """估值工具1年增速PS-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_one_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_ps()

    def page_valuation_tools_ps_func02(self, code):
        """估值工具2年增速PS-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_ps()

    def page_valuation_tools_ps_func03(self, code):
        """估值工具3年增速PS-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_ps()

    def page_valuation_tools_ps_func04(self, code):
        """估值工具1年增速PS-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_one_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_ps()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_valuation_tools_ps_func05(self, code):
        """估值工具2年增速PS-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_ps()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_valuation_tools_ps_func06(self, code):
        """估值工具3年增速PS-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_ps()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_valuation_tools_ps_func07(self, code):
        """估值工具1年增速PS-2022估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_one_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_ps()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()

    def page_valuation_tools_ps_func08(self, code):
        """估值工具2年增速PS-2022估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_ps()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()

    def page_valuation_tools_ps_func09(self, code):
        """估值工具3年增速PS-2022估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()
        sleep(1)
        self.page_click_valuation_pb()
        sleep(1)
        self.page_click_valuation_ps()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()