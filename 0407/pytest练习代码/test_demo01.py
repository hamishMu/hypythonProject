# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/7 23:03
    File: test_demo01.py
Software: PyCharm
______________________________
"""
import pytest


class TestMyDemo:
    def test_a(self):
        print("aaaa")
        assert 'a' == 'a'

    def test_b(self):
        print('bbb')
        assert 'b' == 'b'


if __name__ == '__main__':
    pytest.main(['-s', 'test_demo01.py'])
