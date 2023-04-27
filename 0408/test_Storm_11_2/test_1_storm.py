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
import allure

@allure.feature("测试场景1")
class TestDemo:

    @allure.story("测试用例1-1")
    @allure.severity("trivial")
    def test_1_1(self):
        a = 1+1
        assert  a==2

    @allure.story("测试用例1-2")
    @allure.severity("critical")
    @allure.step("用例2：重要步骤")
    def test_1_2(self):
        assert 2==2