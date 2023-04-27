# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/6 23:34
    File: testhandles.py
Software: PyCharm
测试如果切换窗户handle

______________________________
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)

driver.get("http://hupu.com")
handles = driver.window_handles
print("初始的: ",handles)

driver.find_element(By.LINK_TEXT,'NBA').click()
handles = driver.window_handles
print("点击新闻链接后：: ",handles)



