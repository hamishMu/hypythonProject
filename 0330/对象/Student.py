# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/30 22:47
    File: Student.py
Software: PyCharm
______________________________
"""
from Person import Person


class Student(Person):
    def __init__(self,name,gender,age,school_name,grade):
        # super(Person,self).__init__(name,gender,age)
        super().__init__(name,gender,age)
        self.schoolName = school_name
        self.grade = grade

    def do_homework(self):
        print("学生就要写作业")

    def sleep(self):
        print("学生要每天睡够8小时!")

    def play(self):
        print("学生要加强运动!")
