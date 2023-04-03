# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/3 22:58
    File: test01.py
Software: PyCharm
______________________________
"""
import unittest
"""
执行的顺序
1.先执行setupclass,整个class只执行一遍
2.执行setup,第一个测试用例调用
3.执行第一个测试用例
4.执行teardown,第一个测试用例调用
5.执行setup,第2个测试用例调用
6.执行第2个测试用例
7.执行teardown,第2个测试用例调用
8.最后执行teardonwclass
"""

class TestStorm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupclass")

    def setUp(self):
        print("setup")

    def test_first(self):
        self.assertEqual('storm', 'storm')

    def test_second(self):
        self.assertEqual('second', 'second')

    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


if __name__ == '__main__':

    unittest.main()
