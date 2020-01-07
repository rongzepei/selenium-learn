#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class LearYear():
    u'计算某年师闰年'
    def __init__(self,year):
        self.year = year

    def answer(self):
        year = self.year
        if year % 100 ==0:
            if year % 4 == 0 :
                return "{0}是闰年".format(year)
            else:
                return '{0}不是闰年'.format(year)
        else:
            if year % 4 ==0:
                return '{0}是闰年'.format(year)
            else:
                return '{0}不是闰年'.format(year)