# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/31 11:19
    File: parse_csv.py
Software: PyCharm
______________________________'
解析csv文件中的数据返回一个嵌套列表
"""
import csv


def parse_csv(file):
    mylist = []
    with open(file, 'r', encoding='utf8') as f:
        data = csv.reader(f)
        for i in data:
            mylist.append(i)
        del mylist[0]
    return mylist


if __name__ == '__main__':
    data = parse_csv('my_csv_1.csv')
    print(data)
