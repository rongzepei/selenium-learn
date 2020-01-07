#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest
from test11.leapyear import LearYear

class TestLeapYear(unittest.TestCase):
    def setUp(self):
        print("设置前置条件")

    def tearDown(self):
        print('设置后置条件')

    def test_2000(self):
        ly = LearYear(2000)
        self.assertEqual(ly.answer(),'2000是闰年')

    def test_200(self):
        ly = LearYear(200)
        self.assertNotEqual(ly.answer(),'200是闰年')

if __name__=='__main__':
    unittest.main()