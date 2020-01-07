#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#页面元素的封装
from poium import Page,PageElement,PageElements

class BaiDuPage(Page):
    """
    百度page层，百度页面封装操作到的元素
    """
    search_input = PageElement(id_='kw',timeout=10,describe='百度搜索框')
    search_button = PageElement(id_='su',timeout=5,describe='百度一下按钮')
    #通过timeout可以添加元素超时时间，默认为10s
    #通过describe添加元素描述

    #定义一组元素
    search_result = PageElements(xpath='//div//h3/a')

    """
    poium支持8种定位方法

    elem_id = PageElement(id_='id')
    elem_class = PageElement(class_name='class')
    elem_name = PageElement(name='name')
    elem_tag = PageElement(tag='tagname')
    elem_link_text = PageElement(link_text='this_is_link')
    elem_partila_link_text = PageElement(partila_link_text='is_link')
    elem_xpath = PageElement(xpath='//*[@id="kk"]')
    elem_css = PageElement(css='#id')
    
    """




