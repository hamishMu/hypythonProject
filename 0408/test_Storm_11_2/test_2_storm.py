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
import pytest, allure


class TestDemo2:

    @allure.story("测试用例2-1")
    @allure.severity("minor")
    def test_2_1(self):
        """
        用例描述：这是一个用例的描述
        :return:
        """
        a = 1 + 1
        assert a == 3

    @allure.story("测试用例2-2")
    @allure.severity("minor")
    @allure.step("用例2：重要步骤")
    def test_2_2(self):
        """
        用例描述：这是一个用例的描述
        :return:
        """
        assert  2==2


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/'])
