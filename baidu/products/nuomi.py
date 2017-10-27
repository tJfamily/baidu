from baidu.products.base import BDbase
from baidu.products import NUOMI_PAGE


css_nuomi_logo = ".logo-area > .logo"
css_search_box_nuomi = "#j-searchInput"
css_search_button_nuomi = "#j-searchBtn"

class NuomiPage(BDbase):
    """
        Object model for NuoMi Page of Baidu
    """
    PAGE_IDENTIFIER = NUOMI_PAGE

    def get_nuomi_logo(self):
        logo = self.driver.find_element_by_css_selector(css_nuomi_logo)
        logo_title = logo.get_attribute("title")
        return logo_title

    def search_by_words_nuomi(self, words):
        search_box = self.driver.find_element_by_css_selector(css_search_box_nuomi)
        search_box.send_keys(words)
        search_btn = self.driver.find_element_by_css_selector(css_search_button_nuomi)
        # search_btn.click()
        search_btn.submit()
