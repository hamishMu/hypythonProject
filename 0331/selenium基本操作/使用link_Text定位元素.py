# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/31 16:09
    File: 使用id定位元素.py
Software: PyCharm
______________________________
"""

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")
ele = driver.find_element(By.LINK_TEXT,"新闻")
print(type(ele),ele)
ele.click()

sleep(10)
driver.quit()

# eles = driver.find_elements(By.ID,"kw")
# print(type(eles))