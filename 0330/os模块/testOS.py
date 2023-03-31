# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/30 23:27
    File: testOS.py
Software: PyCharm
______________________________
"""
import os
print("当前系统路径分隔符:",os.sep)
print("工作平台",os.name)
print("当前目录",os.getcwd())

# 目录操作
dirs = os.listdir("G:\pyCharmSpac\HyPythonProject")
print(dirs)