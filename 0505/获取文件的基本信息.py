# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/5/5 17:39
    File: 获取文件的基本信息.py
Software: PyCharm
______________________________
"""
import os
import  datetime
import  time
if os.path.exists("删除文件.py"):
    file_info = os.stat("删除文件.py")
    print("文件完整路径：",os.path.abspath("删除文件.py"))
    print("文件的大小：",file_info.st_size)
    print("最后一次修改时间",time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(file_info.st_mtime)))
