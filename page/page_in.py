from tool.get_driver import GetDriver
from page.page_user_center import PageUserCenter
from page.page_stock_detail_price import PageStockDetailPrice
from page.page_special_stock_toast import PageSpecialStockToast
from page.page_valuation_tools import PageValuationTools
from page.page_valuation_result_subject import PageValuationResultSubject
from page.page_valuation_special_industry_result_subject import PageValuationSpecialIndustryResultSubject
from page.page_valuation_other_stock import PageValuationOtherStock


class PageIn:
    def __init__(self):
        self.driver = GetDriver.get_driver()

    # 获取个人中心页面对象
    @classmethod
    def page_get_user_center(cls):
        return PageUserCenter()

    @classmethod
    def page_get_stock_detail_price(cls):
        return PageStockDetailPrice()

    @classmethod
    def page_get_special_stock_toast(cls):
        return PageSpecialStockToast()

    @classmethod
    def page_get_valuation_tools(cls):
        return PageValuationTools()

    @classmethod
    def page_get_valuation_result_subject(cls):
        return PageValuationResultSubject()

    @classmethod
    def page_get_valuation_special_industry_result_subject(cls):
        return PageValuationSpecialIndustryResultSubject()

    @classmethod
    def page_get_valuation_valuation_other_stock(cls):
        return PageValuationOtherStock()
