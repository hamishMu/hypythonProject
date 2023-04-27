# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/17 15:36
    File: test_001_login.py
Software: PyCharm

用来构建登录的测试用例
______________________________
"""

from selenium import webdriver
import pytest
# 导入本例用到的页面对象文件
from chapter_13.测试框架开发.Test.PageObject import login_page
from chapter_13.测试框架开发.Common import parse_csv

data = parse_csv.my_parse_csv("../../Data/test_001_login.csv")


# data = [('admin', 'jilcad'), ('jack', 'passwd123')]
# ('username', 'password')
# [('admin', 'jack123'), ('jack', 'passwd123'), ('jack', 'passwd12342')]

@pytest.mark.parametrize(data[0], data[1::])
class TestLogin:

    def setup(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get('http://localhost:5000')

    def test_001_login(self, username, password):
        login_page.LoginScenario(self.driver).login(username, password)

    def teardown(self):
        self.driver.quit()
