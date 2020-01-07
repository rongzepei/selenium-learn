#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium import webdriver

"""
一个简单的自动化操作
"""

#初始化一个谷歌驱动
driver = webdriver.Chrome()
#通过驱动打开百度网址
driver.get("http://www.baidu.com")

#通过标签id定位输入框，填写值
driver.find_element_by_id("kw").send_keys("selenium")
#通过标签id定位的提交按钮，点击
driver.find_element_by_id('su').click()

#退出浏览器
driver.quit()