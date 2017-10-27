# -*- coding:utf-8 -*-
from collections import namedtuple


PageID = namedtuple("PageID", "name css_path attr attr_vaule")

HOME_PAGE = PageID(name="Home Page of Baidu",
                   css_path="#u1 > .bri",
                   attr="name",
                   attr_vaule="tj_briicon")

NUOMI_PAGE = PageID(name="NuoMi Page of Baidu",
                    css_path=".logo-area > a",
                    attr="title",
                    attr_vaule="百度糯米")

ZHIDAO_PAGE = PageID(name="ZhiDao Page of Baidu",
                    css_path=".search-cont > a",
                    attr="title",
                    attr_vaule="百度知道")

