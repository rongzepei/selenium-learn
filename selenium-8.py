#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'学习分布式执行'
from selenium.webdriver import Remote,DesiredCapabilities

#引用DesiredCapabilities类的谷歌浏览器配置，才可以启动谷歌浏览器，去调用分布式机器的谷歌浏览器去执行脚本
driver = Remote(desired_capabilities=DesiredCapabilities.CHROME.copy())
driver.get('https://www.baidu.com')
driver.quit()