# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/31 10:05
    File: read_txt.py
Software: PyCharm
______________________________
"""

with open("1.txt","r",encoding="utf8") as f:
    # data1 = f.read()
    # print("读取的文件内容:",data1)
    data2 = f.readline()
    print("data2的内容：",data2)
    data3 = f.readlines()
    print("data3的内容：", data3)