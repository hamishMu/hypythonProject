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


class TestStorm(unittest.TestCase):
    def setUp(self):
        print("setup")

    def test_first(self):
        self.assertEqual('storm', 'storm')

    def tearDown(self):
        print("teardown")


if __name__ == '__main__':
    unittest.main()
