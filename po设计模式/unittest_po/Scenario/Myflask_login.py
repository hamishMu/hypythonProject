# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/8 22:37
    File: Myflask_login.py
Software: PyCharm
用来封装业务场景
______________________________
"""
from selenium import webdriver

from po设计模式.unittest_po.PageObject.login_operations import LoginPage


class LoginScenario:
    """
    这里是定义登录页面的场景
    """


    def login(self):
        # 场景1-登录成功
        url = "http://localhost:5000/login"
        username ='jack'
        password ='passwd123'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(url)
        LoginPage(driver).enter_username(username)
        LoginPage(driver).enter_password(password)
        LoginPage(driver).click_login_button()
        return  driver
