#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from lxml import etree

html = etree.parse('./text.html',etree.HTMLParser())
result = html.xpath("//div[@id='loginDiv']")
print(result)