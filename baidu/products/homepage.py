from selenium.webdriver.common.action_chains import ActionChains as AC

from baidu.products.base import BDbase
from baidu.products import HOME_PAGE


css_search_button = "#su"
css_search_box = "kw"
css_search_img_button = ".soutu-btn"


class HomePage(BDbase):
    """
    Object model for Home Page of Baidu
    """
    PAGE_IDENTIFIER = HOME_PAGE
    css_menu_link = "#u1 > a:nth-child({})"
    css_more_products = "#u > .bri"
    css_more_products_link = ".bdbriwrapper > a:nth-child({})"
    css_all_products_link = ".bdbriwrapper > .bdbrievenmore > a"

    def get_menu_links(self):
        """ To get all the links in the menu bar
        :return： dict(), {link_webelement.text: link_webelement}
        """
        menu_links = dict()
        for i in range(1,9):
            css = self.css_menu_link.format(i)
            link_webelement = self.driver.find_element_by_css_selector(css)
            menu_links[link_webelement.text] = link_webelement
        return menu_links

    def click_menu_link(self, link_text):
        """ Click on the link text in the menu bar to navigate to related website.
            e.g. Click on '新闻' to go to the website of "http://news.baidu.com".
        """
        self.driver.find_element_by_link_text(link_text).click()

    def hover_more_products(self): ### need to research how to locate the webelement "更多产品"
        """ Mouse hover on "更多产品" which next to the "设置" to show more products' picture link"""
        # more_webelement = self.driver.find_element_by_css_selector(self.css_more_products)
        # more_webelement = self.driver.find_element_by_css_selector("div.briimgtitle")
        more_webelement = self.driver.find_element_by_css_selector(self.css_menu_link.format(8))
        # print(more_webelement.text)
        ac = AC(self.driver)
        # ac.move_to_element(more_webelement)
        ac.move_to_element_with_offset(more_webelement, 50, 0)
        ac.perform()

    def get_more_products_links(self):
        """ To get more the products' link in the more products hidden menu.
         :return： dict(), {link_webelement.text: link_webelement}
        """
        mproducts_links = dict()
        for i in range(1, 7):
            css = self.css_more_products_link.format(i)
            link_webelement = self.driver.find_element_by_css_selector(css)
            mproducts_links[link_webelement.text] = link_webelement
        return mproducts_links

    def click_all_products_link(self):
        """ Click on "全部产品" in the hidden menu of "更多产品" to show all products' picture link"""
        self.driver.find_element_by_css_selector(self.css_all_products_link).click()

    def click_product_link(self, link_text):
        link_dicts = self.get_more_products_links()
        link_elems = link_dicts[link_text]
        link_elems.click()

    def get_search_button_text(self):
        return self.driver.find_element_by_css_selector(css_search_button).text

    def search_by_words(self, words):
        search_box = self.driver.find_element_by_css_selector(css_search_box)
        search_box.send_keys(words)
        # self.driver.find_element_by_css_selector(css_search_button).click()
        self.driver.find_element_by_css_selector(css_search_button).submit()

    def search_by_img(self):
        """need to update"""
        pass
