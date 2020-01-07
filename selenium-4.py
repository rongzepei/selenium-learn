#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import csv
import codecs
from itertools import islice   #用于操作迭代对象的函数，返回一个迭代器

from xml.dom.minidom import parse

import json

#模块化，通过把相同的操作封装在一个类内定义一个特定的方法
#如

# class mail:
#     def __init__(self,driver):
#         self.driver = driver
#
#     def login(self,username,passwd):
#         u'一些自动化操作'
#         """
#         login_frame_1 = driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
#         driver.switch_to.frame(login_frame_1)  #进入到framen内嵌页面
#         print("进入到内嵌页面")
#         driver.find_element_by_xpath('//input[@data-loginname="loginEmail"]').send_keys('username')
#         driver.find_element_by_name('password').send_keys('password')
#         driver.find_element_by_id('dologin').click()
#         """
#         pass
#
#     def logout(self):
#         u"退出的操作"
#         pass

"""
封装好之后，只需要调用对应的操作方法即可，方便维护
"""

"""
参数化，把测试数据通过读取文件数据赋值给变量的方式进行，不需要自己每次都手写进取
"""
#常见的读取数据方式
"""
1、从txt文本内读取
2、从csv文件读取
3、从json文件读取
4、从xml文件读取
5、从数据库读取
"""

"""从txt文本内读取"""
# users = []
# with(open('./test.txt','r')) as user_file:
#     data = user_file.readlines()
# for line in data:
#     user = line[:-1].split(":")
#     users.append(user)
# print(users)

"""从csv文件读取数据"""
data = csv.reader(codecs.open('./test.csv','r'))

users = []

#从第二行开始把每一行的数据当作一个列表添加到users这个列表
for line in islice(data,1,None):
    users.append(line)
print(users)

"""读取xml文件"""


# #打开xml文件
# dom = parse('./url.xml')
#
# #得到文档元素对象
# root =dom.documentElement
#
# #获取一组标签
# tag_names = root.getElementsByTagName('url')
#
# #遍历标签组的标签值
# for data in tag_names:
#     print(data.firstChild.data)
#
# logins = root.getElementsByTagName('login')
#
# #获取标签属性值
# username = logins[0].getAttribute('user')
# print(username)

"""
读取json文件内容
"""
# with(open('./scratch.json','r')) as user:
#     data = user.read()
#
# user_list = json.loads(data)
# for user in user_list:
#     print(user)