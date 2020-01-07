#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""""""
"""
常用与自动化测试模拟用户操作的方法
"""
import os

from selenium import webdriver

#模拟鼠标操作需要引入
from selenium.webdriver import ActionChains

#模拟键盘操作需要引入
from selenium.webdriver.common.keys import Keys

#设置元素等待时间
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#引入时间模块
from time import sleep,ctime

#引入下拉框选项模块
from selenium.webdriver.support.select import Select

#滑块操作模块
from selenium.common.exceptions import UnexpectedAlertPresentException

driver= webdriver.Chrome()

# print("设置浏览器窗口的宽高")
# driver.set_window_size(480,800)

first_url = 'http://www.baidu.com'
second_url = 'https://www.cnblogs.com'

# driver.get(first_url)
# driver.get(second_url)
#
# print("返回到上一页")
# driver.back()
#
# print("前进到之前一页")
# driver.forward()
#
# print("刷新界面")
# driver.refresh()

#定位元素的常用方法
"""
clear():清除输入框内容
send_keys(value):模拟按键输入内容
click():单击元素
submit():提交表单
size:返回元素的尺寸
text：获取元素的文本
get_attribute():获得属性值
is_displayer():返回该元素是否用户可见结果
"""

#鼠标操作方法,都封装在actionchains类种
"""
perform():执行ActionChains类中存储的所有行为
context_clickk():右击
double_click():双击
drag_and_drop():拖动
move_to_element():鼠标悬停
"""
# driver.get(first_url)
# above = driver.find_element_by_link_text('设置')
# ActionChains(driver).move_to_element(above).perform()


#模拟键盘操作
"""
send_keys(Keys.BACK_SAPCE):删除键
send_keys(Keys.SPACE):空格键
send_keys(Keys.TAB):TAB键
send_keys(Keys.ESCAPE):回退键
send_keys(keys.ENTER):回车键
send_keys(keys.CONTROL,'a'):全选（ctrl+a）
send_keys(keys.CONTROL,'c'):复制（ctrl+c）
send_keys(keys.CONTROL,'x'):剪切（ctrl+x）
send_keys(keys.CONTROL,'v'):粘贴（ctrl+v）
send_keys(Keys.(F1-F12)):F1-F2
"""


#获得验证信息:用于进行结果校验
"""
title:获取当前页面的标题
current_url : 获取当前页面的url
text:用于获取当前页面的文本信息
"""


"""显示等待"""
# try:
#     element = WebDriverWait(driver,5,0.5).until(
#       EC.presence_of_element_located((By.ID,'kw1')),message='超时找不到元素'
#     )
# except BaseException as e:
#     print(e)
# else:
#     element.send_keys('selenium')


""""自己通过元素是否可见设置显示等待"""
# for i in range(10):
#     try:
#         element_1 = driver.find_element_by_id('kw1')
#         if element_1.is_displayed():
#             break
#     except:
#         pass
#     sleep(1)
# else:  #else用于判断是否有执行break跳出循环，如果没有跳出则执行else内容
#     print("time out")
#
# print(ctime())

"""隐式等待"""
#设置隐式等待10秒
# driver.implicitly_wait(10)
# try:
#     print(ctime())
#     driver.get(first_url)
#     driver.find_element_by_id('kw1')
# except BaseException as e:
#     print(e)
# finally:
#     print(ctime())
# driver.quit()


"""定位一组元素,在element后加一个s"""
# driver.get(first_url)
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('su').click()

#显示等待
# try:
#     print(ctime()) #输出当前时间
#     element = WebDriverWait(driver,5,0.5).until(
#       EC.presence_of_element_located((By.XPATH,"//div[@tpl='se_com_default']/h3/a")),message='超时找不到元素'
#     )
# except BaseException as e:
#     print(e)
#
# #当不加上元素查看判断时，容易出现无法找到元素的情况
# texts = driver.find_elements_by_xpath("//div[@tpl='se_com_default']/h3/a")
#
# #计算匹配的结果计数
# print(len(texts))
# for text in texts:
#     print(text.text)

"""多表单切换"""
# #用于解决表单内嵌页面的元素定位
#
# driver.get('http://www.126.com')
# sleep(10)
# #
# login_frame_1 = driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
# driver.switch_to.frame(login_frame_1)  #进入到framen内嵌页面
# print("进入到内嵌页面")
# driver.find_element_by_xpath('//input[@data-loginname="loginEmail"]').send_keys('username')
# driver.find_element_by_name('password').send_keys('password')
# driver.find_element_by_id('dologin').click()
# driver.switch_to.default_content()  #返回到最外层页面
# print('返回到外层页面')

"""
多窗口切换
current_window_handle:获得当前按窗口句柄
window_handles:返回所有窗口的句柄到当前会话
switch_to_window():切换到想要的窗口

"""
# driver.implicitly_wait(10)
# driver.get(first_url)

#获得百度搜索的窗口
# search_windows = driver.current_window_handle
#
# driver.find_element_by_link_text('登录').click()
# driver.find_element_by_link_text('立即注册').click()
#
# #获得当前所有打开的窗口的句柄
# all_handle = driver.window_handles

#进入注册界面
# for handle in all_handle:
#     if handle != search_windows:
#         driver.switch_to_window(handle)
#         print(driver.title)
#         driver.find_element_by_name('userName').send_keys('username')
#         driver.find_element_by_name('phone').send_keys('138xxxxxxxx')
#         sleep(10)
#
# driver.switch_to_window(search_windows)
# print(driver.title)
# sleep(10)
#
# driver.quit()


"""
警告框处理
先使用switch_to_alert()定位
text:返回alert、confirm、prompt中的信息
accept():接受现有警告框
dismiss():解散现有警告框
send_keys(在警告框内输入内容，如果可以的输入的话)
"""
#
# driver.get(first_url)
#
# #打开搜索设置
# link = driver.find_element_by_link_text("设置").click()
# driver.find_element_by_link_text('搜索设置').click()
# sleep(2)
#
# #保存设置
# driver.find_element_by_class_name('prefpanelgo').click()
# sleep(10)
#
# #获取警告框
# alert = driver.switch_to_alert()
#
# alert_text = alert.text
# print(alert_text)
#
# #接受警告框
# alert.accept()#点击确定按钮
#
# sleep(10)
# driver.quit()


"""
下拉框处理
使用select类处理
select_by_value():通过value值定位下拉选项
select_by_visibe_text():通过text值定位下拉选项
select_by_index():根据下拉选项的索引进行选择，第一个选项为0 
"""
#
# driver.get(first_url)
# sleep(5)
#
# driver.find_element_by_link_text('设置').click()
# driver.find_element_by_link_text('搜索设置').click()
#
# #定位到下拉框  元素没有加载完时取进行操作容易返回元素查找失败，记得添加延时
# sleep(2)
# select_1= Select(driver.find_element_by_xpath('//select[@id="nr"]'))
#
# select_1.select_by_value('20')
# sleep(2)
#
# select_1.select_by_index(0)
# sleep(2)
#
# select_1.select_by_visible_text('每页显示50条')
#
# sleep(10)
# driver.quit()


"""
实现文件上传的思路
selenium 没有对应的文件上传方法
常见的两种web文件上传方法：
1、通过将本地文件路径当作一个值，放在input标签通过，通过form表单提交给服务器
2、通过flash、ajax、js技术实现上传

对于第一种：我们只需要把本地文件路径send_keys给input标签就好了
第二种：司用autolt插肩结合selenium实现
"""

"""
实现文件下载
在操作文件下载时，需要对浏览器进行设置，一个是设置禁止下载弹窗，一个是设置下载文件的路径
"""

# #设置谷歌浏览器配置对象
# options = webdriver.ChromeOptions()
#
# prefs = {
#     'profile.default_content_settings.popups':0,  #设置禁止下载弹窗
#     'download.default_directory':os.getcwd()      #设置下载文件的保存路径
# }
# options.add_experimental_option('prefs',prefs)
#
# driver.get("https://pypi.org/project/selenium/#files")
# sleep(10)
# driver.find_element_by_link_text('selenium-3.141.0.tar.gz').click()

"""
操作cookies
get_cookies():获得所有cookies
get_cookie(name):获得字典中key为"name"的cookies
add_cookie(cookie_dit):添加cookie
delete_cookie(name,optionsString):删除名为optionsString的cookie
delete_all_cookies():删除所有cookies
"""
#
# driver.get(first_url)
#
# #获取所有cookies
# # cookies = driver.get_cookies()
#
# #手动添加cookies
# driver.add_cookie({'name':"haha",'value':'1231231'})
# for cookie in driver.get_cookies():
#     print('name: %s -->  value:   %s' % (cookie['name'],cookie['value']))
#
# #删除特定的cookie
# driver.delete_cookie(u'haha')
# for cookie in driver.get_cookies():
#     print('name: %s -->  value:   %s' % (cookie['name'],cookie['value']))
# #删除所有cookie
# driver.delete_all_cookies()
# sleep(5)
# driver.quit()

"""
调用JS
通过execute_script(js代码)方法实现
有些无法通过定位元素进行操作的，可以通过调用js代码去实现
"""

# driver.get(first_url)
# driver.set_window_size(400,800)
# sleep(5)
# js = 'window.scrollTo(100,450)'
# driver.execute_script(js)
#
# sleep(10)
# driver.quit()

"""
处理html5视频播放
"""
# driver.get("http://videojs.com")
#
# sleep(50)
#
# video = driver.find_element_by_xpath("//*[@id='preview-player_html5_api']")
# print('aaa')
# #返回播放文件地址
# url = driver.execute_script("return arguments[0].currentSrc;",video)
# print(url)
#
# #播放视频
# print("strat")
# driver.execute_script('arguments[0].play()',video)
#
# sleep(15)
#
# print('stop')
# driver.execute_script('arguments[0].pause()',video)
#
# driver.quit()

"""
滑动解锁
click_and_hold():单击并按下鼠标左键
move_by_offset():移动鼠标，第一个参数为x坐标距离，第二个参数为y坐标距离
reset_action():重置action
"""
# driver.get("https://www.helloweba.net/demo/2017/unlock/")
#
# sleep(50)
# #定位滑块
# slider = driver.find_elements_by_class_name('slide-to-unlock-handle')[0]
# action = ActionChains(driver)
# action.click_and_hold(slider).perform()
#
# for index in range(200):
#     try:
#         action.move_by_offset(2,0).perform()
#     except UnexpectedAlertPresentException:
#         break
#     action.reset_actions()
#     sleep(0.1)
#
# success_text= driver.switch_to_alert().text
# print(success_text)
# driver.quit()


"""
屏幕截图
"""
# driver.get(first_url)
# driver.save_screenshot('./files/baidu.png')
# driver.quit()

"""
关闭窗口
close(),用于关闭当前窗口
"""