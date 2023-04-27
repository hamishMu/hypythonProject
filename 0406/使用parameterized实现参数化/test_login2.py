# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/6 16:11
    File: test_login2.py
Software: PyCharm
______________________________
"""

from selenium import webdriver
import  unittest
from parameterized import parameterized,param
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):
    def setUp(self) :
        self.driver =webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # 访问登录页面
        self.driver.get('http://localhost:5000/login')

    # @parameterized.expand，括号中传递列表
    # 列表中传递元组，每一个元组是一个测试用例
    @parameterized.expand([('jack','passwd123')])
    def test_001_login(self,username,password):
        # 登录名
        login_name = self.driver.find_element(By.NAME, 'username')
        login_name.clear()
        login_name.send_keys(username)
        # 登录密码
        login_password = self.driver.find_element(By.NAME, "password")
        login_password.clear()
        login_password.send_keys(password)
        # 登录按钮
        login_btn = self.driver.find_element(By.XPATH, '/html/body/form/input[3]')
        login_btn.click()

        message = '登录成功'
        self.assertIn(message, self.driver.page_source)

    def tearDown(self) -> None:
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()