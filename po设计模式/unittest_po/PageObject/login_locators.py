# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/8 22:21
    File: login_locators.py
Software: PyCharm
______________________________
"""
from selenium.webdriver.common.by import By


class LoginPageLocators:
    """
    用户登录页面
    """
    Username = (By.NAME, "username")
    Password = (By.NAME, "password")
    LoginButton = (By.XPATH, '/html/body/form/input[3]')
