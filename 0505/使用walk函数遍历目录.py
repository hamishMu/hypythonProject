# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/5/5 17:27
    File: 使用walk函数遍历目录.py
Software: PyCharm

os模块中的walk函数
______________________________
"""
import  os
# 遍历G:\pyCharmSpac\HyPythonProject\0505
path = 'G:/pyCharmSpac/HyPythonProject/0505'
tuples = os.walk(path)
for tuple1 in tuples:
    print(tuple1,'\n')
