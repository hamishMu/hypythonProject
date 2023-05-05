# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/5/5 17:20
    File: 读取文件.py
Software: PyCharm
______________________________
"""

file_name = '1.txt'
with open(file_name,'r',encoding='utf8')as f:
    # content = f.read()
    content = f.readlines()
    print(content)