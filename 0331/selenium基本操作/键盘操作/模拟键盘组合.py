# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/31 17:48
    File: 模拟键盘组合.py
Software: PyCharm
______________________________
"""

from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
# 通过sendkey方法模拟输入文字
driver.find_element(By.ID,'kw').send_keys('自动化测试招聘')
sleep(3)
driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'a')
driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'c')

# 通过clear方法清楚搜索框中的内容
driver.find_element(By.ID,'kw').clear()
sleep(3)


driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'v')
sleep(4)
driver.quit()


