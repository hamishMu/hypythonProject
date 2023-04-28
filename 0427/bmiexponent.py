# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/27 18:06
    File: bmiexponent.py
Software: PyCharm
计算BMI指数
体重/身高*身高
______________________________
"""


def BMI(weight, height):
    try:
        result = weight *1.0/ (height * height)

    except Exception as e:
        print(e)
    return result


def judgment_bmi(result):
    if result < 18.5:
        print("您的体重过轻")
    elif result < 24.9:
        print("正常范围，注意保持")
    elif result < 29.9:
        print("您的体重过重")
    else:
        print("肥胖，为了健康请减重!")


if __name__ == '__main__':
    while True:
        q= input("正常开始程序请输入1，退出程序输入q|Q:\n")
        if q == "q" or q =="Q":
            break
        else:
            w = input("请输入您的体重：")
            h = input("请输入您的身高: ")
            r = BMI(float(w), float(h))
            judgment_bmi(r)

