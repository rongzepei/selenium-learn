#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#创建被测试文件

#计算器类
class Calculator:
    u"""
    用于完成两个输的加减乘除
    """
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b