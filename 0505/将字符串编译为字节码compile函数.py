# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/5/5 16:03
    File: 将字符串编译为字节码compile函数.py
Software: PyCharm
compile():
source:字符串
filename:代码文件名称
mode:指定编译代码的种类，可以指定为eval，exec,single
flags:变量作用域
______________________________
"""

code1 = """
for i in range(0,20):
    if i %2 == 0:
        print(i,end=",")
"""
byteExec = compile(code1,'','exec')
print(type(byteExec))
exec(byteExec)


