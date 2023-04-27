# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/17 16:38
    File: parse_csv.py
Software: PyCharm
解析csv文件
______________________________
"""

import csv


def my_parse_csv(fileName):
    with open(fileName, 'r', encoding='utf8') as f:
        data = []
        data_csv = csv.reader(f)
        print(data_csv)
        for i in data_csv:
            print(type(i))
            data.append(tuple(i))
    return data


if __name__ == '__main__':
    mydata = my_parse_csv("../Data/test_001_login.csv")
    print(mydata[0], type(mydata[0]))
    print(mydata[1::])
