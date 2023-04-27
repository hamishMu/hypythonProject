# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/8 17:49
    File: test_1_storm.py
Software: PyCharm
______________________________
"""
import pytest


class TestStorm1:
    @pytest.mark.L1
    def test_01(self):
        print('aaaa')
        assert 'a' == 'a'
