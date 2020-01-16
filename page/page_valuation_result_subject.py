from time import sleep
import page
from base.base import Base


class PageValuationResultSubject(Base):
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

    def page_click_result_subject(self):
        """结果科目"""
        self.base_click(page.result_subject)

    def page_click_every_profit(self):
        """每股净利润"""
        self.base_click(page.every_profit)

    def page_click_every_property(self):
        """每股净资产"""
        self.base_click(page.every_property)

    def page_click_every_market(self):
        """每股净销售"""
        self.base_click(page.every_market)

    def page_get_valuation_result(self):
        """获取我的估值结果"""
        result = self.base_get_text(page.valuation_result)
        return float(result)

    def page_result_subject_pe_func01(self, code):
        """结果科目1年增速PE-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_one_year_growth_rate()

    def page_result_subject_pe_func02(self, code):
        """结果科目2年增速PE-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()

    def page_result_subject_pe_func03(self, code):
        """结果科目3年增速PE-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()

    def page_result_subject_pe_func04(self, code):
        """结果科目1年增速PE-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_one_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_result_subject_pe_func05(self, code):
        """结果科目2年增速PE-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_result_subject_pe_func06(self, code):
        """结果科目3年增速PE-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_result_subject_pe_func07(self, code):
        """结果科目1年增速PE-2022估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_one_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()

    def page_result_subject_pe_func08(self, code):
        """结果科目2年增速PE-2022估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()

    def page_result_subject_pe_func09(self, code):
        """结果科目3年增速PE-2022估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()

    def page_result_subject_pb_func01(self, code):
        """结果科目2年增速PB-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_every_profit()  # 选择
        sleep(1)
        self.page_click_every_property()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()

    def page_result_subject_pb_func02(self, code):
        """结果科目2年增速PB-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_every_profit()  # 选择
        sleep(1)
        self.page_click_every_property()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_result_subject_pb_func03(self, code):
        """结果科目2年增速PB-2022估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_every_profit()  # 选择
        sleep(1)
        self.page_click_every_property()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_two_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()

    def page_result_subject_ps_func01(self, code):
        """结果科目3年增速PS-2020估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_every_profit()  # 选择
        sleep(1)
        self.page_click_every_market()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()

    def page_result_subject_ps_func02(self, code):
        """结果科目3年增速PS-2021估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_every_profit()  # 选择
        sleep(1)
        self.page_click_every_market()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2021()

    def page_result_subject_ps_func03(self, code):
        """结果科目3年增速PS-2022估值组合业务方法"""
        self.page_input_stock_code(code)
        sleep(1)
        self.page_click_search_btn()
        sleep(1)
        self.page_click_result_subject()
        self.page_click_every_profit()  # 选择
        sleep(1)
        self.page_click_every_market()
        sleep(1)
        self.page_click_select_growth_rate()
        sleep(1)
        self.page_click_three_year_growth_rate()
        sleep(1)
        self.page_click_select_date()
        sleep(1)
        self.page_click_date2022()

