# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/30 15:07
    File: webdriver脚本示例.py
Software: PyCharm
______________________________
"""

from selenium import webdriver
import unittest


class VisitPTPress(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Edge()

    def test_open_ptpress(self):
        self.driver.get("https://www.ptpress.com.cn")
        self.assertIn("图书", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
