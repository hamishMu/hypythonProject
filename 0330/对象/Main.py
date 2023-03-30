# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/30 22:58
    File: Main.py
Software: PyCharm
______________________________

测试类
"""
from Person import Person
from Student import Student

if __name__ == '__main__':
    p = Person("jack", "男", 30)
    print('姓名是:', p.name)
    print('性别:', p.gender)
    print('年龄:', p.age)
    p.walk()
    p.eat()
    p.sleep()
    p.speak()
    s = Student("mark","女",24,"清华大学","研究生1")
    print('姓名是:', s.name)
    print('性别:', s.gender)
    print('年龄:', s.age)
    s.speak()
    s.play()
    s.sleep()
