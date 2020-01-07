#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import csv
import codecs
from itertools import islice

import unittest
from time import sleep
from selenium import webdriver
from parameterized import parameterized  #python自带的参数化模块
from ddt import ddt,data,file_data,unpack  #针对unittest设计的参数化模块

from test11.page_object import BaiDuPage
"""
使用ddt进行参数化，要记得给类加上ddt装饰器
"""

@ddt
class TestBaidu(unittest.TestCase):

    u'当后置前置条件不需要频繁复用到每个测试用例，可以把前置和后置条件放在setupclass和teardownclass内'
    @classmethod
    def setUpClass(cls):
        print('开始执行测试用例')
        cls.driver = webdriver.Chrome()
        cls.base_url='https://www.baidu.com'

        #参数的读取放在setupclass内 ，利用读取文件的方式进行参数化
        # cls.test_data=[]
        # with codecs.open('../test.csv', 'r') as fp:
        #     data = csv.reader(fp)
        #     for line in islice(data, 1, None):
        #         cls.test_data.append(line[1])

    def setUp(self):
        print("设置每一条用例的前置条件")

    def tearDown(self):
        print("设置每一条用例的后置条件")

    def baidu_search(self,search_key):
        page = BaiDuPage(self.driver)
        page.get(self.base_url)
        page.search_input = search_key
        page.search_button.click()
        sleep(4)
        title = self.driver.title
        self.assertEqual(title,'{0}_百度搜索'.format(search_key))

    """
    引入parameterized参数化模块，先在测试用例前定义该装饰器，在内部添加元组数据，在name对应的是第一列的数据，search_key对应的是第二列的数据
    如：
    name    search_key
    case1   seleniumun
    case2   unittest
    
    每一组元组数据对应执行一条测试用例，所以该用例会根据元组数据执行多次用例，且参数化会自动加上0.1.2来区分每条测试用例，name值也会作为每条用例的后缀
    """

    @parameterized.expand([
        ('case1','selenium'),
        ('case2','unittest'),
        ('case3','parameterized')
    ])
    def test_1(self,name,search_key):
        u'使用第一行数据进行测试'
        self.baidu_search(search_key)

    #ddt参数化使用方式1  使用列表方式
    @data(['case4','ddt'],['case5','xpath'],['case6','python'])
    @unpack
    def test_2(self,case,search_key):
        print("第一种ddt参数化使用方式",case)
        self.baidu_search(search_key)
    #
    # ddt参数化使用方式2  使用元组方式
    @data(('case7', 'ddt'), ('case8', 'xpath'), ('case9', 'python'))
    @unpack
    def test_3(self, case, search_key):
        print("第二种ddt参数化使用方式")
        self.baidu_search(search_key)

    #ddt参数化使用方式3  使用字典方式
    @data({'search_key':'ddt'}, {'search_key': 'xpath'}, {'search_key':'python'})
    @unpack
    def test_4(self,  search_key):
        print("第三种ddt参数化使用方式")
        self.baidu_search(search_key)


    #参数化读取json文件
    @file_data('../test.json')
    def test_5(self,search_key):
        print('通过ddt内部装饰器读取json文件数据')
        self.baidu_search(search_key)

    @classmethod
    def tearDownClass(cls):
        print('结束执行测试用例')
        print("浏览器退出")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2 )

