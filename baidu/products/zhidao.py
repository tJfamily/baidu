from baidu.products.base import BDbase
from baidu.products import ZHIDAO_PAGE


css_zhidao_logo = ".search-cont.clearfix > .logo"
css_search_box_zhidao = "#kw"
css_search_button_zhidao = "#search-btn"


class ZhidaoPage(BDbase):
    """
        Object model for ZhiDao Page of Baidu
    """
    PAGE_IDENTIFIER = ZHIDAO_PAGE

    def get_zhidao_logo(self):
        logo = self.driver.find_element_by_css_selector(css_zhidao_logo)
        return logo.text

    def search_by_words_zhidao(self, words):
        search_box = self.driver.find_element_by_css_selector(css_search_box_zhidao)
        search_box.send_keys(words)
        search_btn = self.driver.find_element_by_css_selector(css_search_button_zhidao)
        search_btn.click()
        # search_btn.submit()
