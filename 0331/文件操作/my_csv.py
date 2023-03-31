# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/31 11:17
    File: my_csv.py
Software: PyCharm
______________________________
"""
import  csv
with open('my_csv_1.csv','r',encoding='utf8')as f:
    data = csv.reader(f)
    print(data)
    for i in data:
        print(i)