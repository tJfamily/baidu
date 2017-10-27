from baidu.products.homepage import HomePage
from baidu.products.nuomi import NuomiPage
from baidu.products.zhidao import ZhidaoPage


class BDProducts(object):
    """ Page object model for baidu products: home page, nuomi, zhidao"""
    def __init__(self, driver):
        self.driver = driver
        self.homepage = HomePage(driver)
        self.nuomipage = NuomiPage(driver)
        self.zhidaopage = ZhidaoPage(driver)
