# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/5/5 17:36
    File: 删除文件.py
Software: PyCharm
使用os模块中的remove.
首先判断文件是否存在
______________________________
"""
import  os
p = '高级文件操作函数.txt'
if os.path.exists(p):
    os.remove(p)
    print("文件删除完毕！")
else:
    print("文件不存在")
