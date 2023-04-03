
# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/31 15:24
    File: 网页前进后退.py
Software: PyCharm

driver.back()
driver.forward()
driver.refresh()
______________________________
"""
from selenium import webdriver
from  time import sleep


driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
print("当前网页的title",driver.title)
sleep(2)
print("当前浏览器窗口的{}".format(driver.get_window_size()))
driver.get("https://www.ptpress.com.cn")
print("获取当前页面的url地址:",driver.current_url)
print("当前网页的title",driver.title)
print("将浏览器窗口最大化")
driver.maximize_window()
sleep(2)
# 通过back方法进行后退到百度首页
driver.back()

sleep(2)

# 通过forward方法前进
driver.forward()
sleep(2)

driver.quit()