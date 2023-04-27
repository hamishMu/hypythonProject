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
from po设计模式.MyPytest.pageobject import login_page

data = [('admin', 'jilcad'), ('jack', 'passwd123')]


@pytest.mark.parametrize(('username', 'password'), data)
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


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', '../report/'])
