# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/6 21:47
    File: myCodeV0.1.py
Software: PyCharm
______________________________
"""
import datetime
import time

testdate = "2022-01-01 15:00:35"

testdate = datetime.datetime.strptime(testdate, '%Y-%m-%d %H:%M:%S')

now = datetime.datetime.now()
print(now)
print(testdate)
testdate = datetime.datetime.strftime(testdate, '%Y年%m月%d日')
print("当前系统日期为:{}".format(datetime.datetime.now()))