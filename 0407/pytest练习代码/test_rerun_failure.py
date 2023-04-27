# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/7 23:47
    File: test_rerun_failure.py
Software: PyCharm
______________________________
"""


class TestRerunFailures:
    def test_a(self):
        print("aaaa")
        assert 'a' == 'a'

    def test_b(self):
        print('bbb')
        assert 'b' == 'c'
