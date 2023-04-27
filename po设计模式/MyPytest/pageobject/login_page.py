# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/17 15:23
    File: login_page.py
Software: PyCharm
封装第一层，页面元素查找层
______________________________
"""
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def find_username(self):
        ele = self.driver.find_element(By.NAME,'username')
        return ele

    def find_password(self):
        ele = self.driver.find_element(By.NAME,'password')
        return ele

    def find_login_btn(self):
        ele = self.driver.find_element(By.XPATH, '/html/body/form/input[3]')
        return  ele


"""
元素操作类
"""
class LoginOper:
    def __init__(self,driver):
        self.login_page  =LoginPage(driver)

    def input_username(self,username):
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)

    def input_password(self,password):
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(password)

    def click_login_btn(self):
        self.login_page.find_login_btn().click()


"""
业务场景类
"""
class LoginScenario:
    def __init__(self,driver):
        self.login_oper = LoginOper(driver)

    def login(self,username,password):
        self.login_oper.input_username(username)
        self.login_oper.input_password(password)
        self.login_oper.click_login_btn()

