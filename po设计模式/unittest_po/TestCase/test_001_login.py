# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/8 22:50
    File: test_001_login.py
Software: PyCharm


SessionNotCreatedException:chrome更新后，驱动没有更新。
______________________________
"""
from parameterized import parameterized
from selenium import webdriver
from po设计模式.unittest_po.PageObject.login_operations import LoginPage
import unittest

url = 'http://localhost:5000/login'


class LoginTest(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(url)

    @parameterized.expand([('admin', 'passwd123')])
    def test_login(self, username, password):
        LoginPage(self.driver).enter_username(username)
        LoginPage(self.driver).enter_password(password)
        LoginPage(self.driver).click_login_button()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
