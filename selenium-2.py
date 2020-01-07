#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""""""
"""
常用的定位方法
"""

#8种元素定位方法

#id定位：find_element_by_id()  通过标签的id查找元素

#name定位:find_element_by_name()  通过标签的name属性查找元素

#class定位;find_element_by_class_name()  通过标签的class定位元素

#tag定位：find_element_by_tag_name()  通过标签名定位元素

#link定位：find_element_by_link_text()  通过元素标签对之间的文字信息定位link元素

#partial link定位：find_element_by_partial_link_text()  通过取文字连接的部分文字进行定位

#xpath定位：find_element_by_xpath()
# 通过绝对路径/元素属性/层级与属性结合/使用逻辑运算符/使用contains方法/使用text方法进行定位

#css定位：find_element_css_selector
#通过class/id/标签名/标签层级关系/属性/组合定位

"""
还有另一套写法
"""
"""
调用find_element()这个方法
find_element(BY.ID,'kw')
find_element(BY.CLASS_NAME,'ws')
find_element(BY.NAME,'kw')
find_element(BY.TAG_NAME,'kw')
find_element(BY.LINK_TEXT,'新闻')
find_element(BY.PARTIAL_LINK_TEXT,'新')
find_element(BY.XPATH,'kw')
find_element(BY.CSS_SELECTOR,'kw')
"""


