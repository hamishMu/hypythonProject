# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/5/5 15:49
    File: 高级字符串内置函数_eval.py
Software: PyCharm
eval函数：执行一个字符串表达式并返回执行结果
______________________________
"""
print(eval("1+2+3+4+5+6"))
n = 2
print(eval("n+251"))
print(eval("n*251"))
print(eval("pow(n,3)"))
s = input("请输入一个算术题：")
print(eval(s))



"""
eval函数实现数据类型之间的转换
"""
a = "[99,33,78,65]"
b = "(20,10,44)"
c = "514"
print(a,"转换前:",type(a))
print(a,"转换后:",type(eval(a)))
print(b,"转换前:",type(b))
print(b,"转换后:",type(eval(b)))
print(c,"转换前:",type(c))
print(c,"转换后:",type(eval(c)))