# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/31 17:37
    File: 鼠标悬浮.py
Software: PyCharm
______________________________
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("http://www.baidu.com/")
driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
source = driver.find_element(By.ID,"dragger")
target = driver.find_element(By.XPATH,'/html/body/div[2]')
sleep(2)
# 通过drag_and_drop方法进行模拟鼠标拖动操作
ActionChains(driver).drag_and_drop(source,target).perform()
sleep(10)

driver.quit()