# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/30 22:42
    File: Person.py
Software: PyCharm
______________________________
"""


class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    # 定义方法
    def speak(self):
        print("人可以说话")

    def walk(self):
        print("人可以走路")

    def sleep(self):
        print("人可以睡觉")

    def eat(self):
        print("人可以吃食物")
