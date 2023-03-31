# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/31 10:29
    File: operate_json.py
Software: PyCharm
______________________________
json模块用于字符串和json数据类型的转换
有四个功能
dumps,dump,load,loads
dumps：将字典转化为字符串
"""
import  json
dict1={"name": "storm","age": 30,"sex": "男"}
print(dict1,type(dict1))
# dumps将字典转为字符串
j1 = json.dumps(dict1)
print(j1,type(j1))
print("*"*20)
# dump将字典转为字符串，并写入json文件中


with open("4.json","w")as f:
    j2 = json.dump(dict1,f)
    print(j2,type(j2))

