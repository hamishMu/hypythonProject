# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/8 17:23
    File: test_remark.py
Software: PyCharm
______________________________
"""
"""
pytest提供了标记机制，借助mark关键字，可以对测试函数，类，方法进行标记

pytest -s "test_remark.py"
"""

import  pytest

class Test01:
    @pytest.mark.L1
    @pytest.mark.L2
    def test_a(self):
        print('aaaaa')
        assert 'a'=='a'

    @pytest.mark.L2
    def test_b(self):
        print('bbbbb')
        assert 'b' == 'b'

class Test02:
    @pytest.mark.L1
    def test_c(self):
        print('cccccc')
        assert 'c'=='c'

    @pytest.mark.L3
    def test_d(self):
        print('dddddd')
        assert 'd' == 'd'


