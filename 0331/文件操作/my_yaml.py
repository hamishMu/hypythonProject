# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/31 11:07
    File: my_yaml.py
Software: PyCharm
______________________________
"""
import yaml

with open('1.yaml','r',encoding="utf8")as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
    print(data,type(data))
    print(data['websites']['URL'])
    print(data['websites']['IP'])
    print(data['websites']['PORT'])