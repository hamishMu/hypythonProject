# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/8 22:26
    File: login_operations.py
Software: PyCharm
______________________________
"""
from po设计模式.unittest_po.PageObject.login_locators import LoginPageLocators


class BasePage:
    # 构造一个基础类
    def __init__(self,driver):
        self.driver = driver



class LoginPage(BasePage):


    # 用户登录页面的元素操作
    def enter_username(self, username):
        # 输入用户名
        ele = self.driver.find_element(*LoginPageLocators.Username)
        ele.clear()
        ele.send_keys(username)

    # 输入密码
    def enter_password(self, password):
        # 输入用户名
        ele = self.driver.find_element(*LoginPageLocators.Password)
        ele.clear()
        ele.send_keys(password)

    # 点击登录按钮

    def click_login_button(self):
        # 输入用户名
        ele = self.driver.find_element(*LoginPageLocators.LoginButton)
        ele.click()
