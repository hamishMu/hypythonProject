# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/7 23:07
    File: test_demo_func.py
Software: PyCharm
______________________________
"""

import pytest


def test_a():
    print('aaaa')
    assert 'a' == 'a'


def test_b():
    print('bbbbb')
    assert 'b' == 'b'


if __name__ == '__main__':
    pytest.main(['-s'])
