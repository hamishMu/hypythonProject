# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/5/5 15:58
    File: 执行存储在字符串或文件中的python代码函数exec.py
Software: PyCharm

exec()函数用于执行存储在字符串或者文件中的python语句，与eval相比，exec()函数可以执行更复杂的代码
______________________________
"""

code = """
import  random
i = 0
list1 = []
while i<10:
    list1.append(random.randint(0,100))
    i+=1
print(list1)
"""

if __name__ == '__main__':
    exec(code)

