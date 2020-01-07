#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

#把测试结果发送给负责人
import smtplib
from email.mime.text import MIMEText
from email.header import Header

import yagmail
import zipfile,os

#定义发邮件的函数
def send_email(time,report):
    yag = yagmail.SMTP(user='1617265674@qq.com',password='vvdyneaymjbbddhf',host='smtp.qq.com')
    subjects = time+'自动化测试报告'
    contents = '正文，请看附件'
    yag.send('rongzepei@gosuncn.com',subjects,contents,[report])



if __name__=='__main__':

    dir = './test11/'
    suits = unittest.defaultTestLoader.discover(dir, pattern='test*.py')

    now_time = time.strftime("%Y-%m-%d %H_%M_%S")  # 通过时间模块来定义每一次运行自动化测试的报告
    report = './'+now_time+'测试报告.html'

    fp = open(report,'wb')
    #用于生成测试报告
    runner = HTMLTestRunner(stream=fp,title='测试用例执行报告',description='运行环境：win10,谷歌浏览器')
    # runner = unittest.TextTestRunner()
    runner.run(suits)
    fp.close()

    #有些html文件通过邮箱发送会不以html附件形式发送，这时候可以考虑将其压缩后当作附件发送
    zipname = now_time+'测试报告.zip'
    fzip = zipfile.ZipFile(zipname,'w',zipfile.ZIP_DEFLATED)
    fzip.write(report)
    fzip.close()

    # 使用yagmail发送附件只需要指定本地文件的路径即可
    send_email(now_time,zipname)