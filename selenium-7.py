#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
压缩文件
"""
import zipfile,os

filepath = './report.html'
zipname = 'report.zip'
#创建zip对象
fzip = zipfile.ZipFile(zipname,'w',zipfile.ZIP_DEFLATED)
#写入要压缩的文件
fzip.write(filepath)
fzip.close()