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


class TestStorm2:
    @pytest.mark.L2
    def test_02(self):
        print('bbbbb')
        assert 'b' == 'c'