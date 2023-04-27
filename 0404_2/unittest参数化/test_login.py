# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/4 19:42
    File: test_login.py
Software: PyCharm
______________________________
"""
from selenium import webdriver
import unittest
import ddt
from selenium.webdriver.common.by import By
"""
1.@ddt.data，括号中可以传递列表或元组
2@ddt.unpack解包

"""

# @ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问登录页面
        self.driver.get("http://localhost:5000/login")

    # @ddt.data(['admin', 'error'], ['jack', 'passwd123'])
    # @ddt.unpack
    # def test_001_login(self, username, password):
    def test_001_login(self):
        # 登录名
        login_name = self.driver.find_element(By.NAME, 'username')
        login_name.clear()
        login_name.send_keys('jack')
        # 登录密码
        login_password = self.driver.find_element(By.NAME, "password")
        login_password.clear()
        login_password.send_keys('passwd123')
        # 登录按钮
        login_btn = self.driver.find_element(By.XPATH, '/html/body/form/input[3]')
        login_btn.click()

        message = '登录成功'
        self.assertIn(message, self.driver.page_source)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
