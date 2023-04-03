# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/31 17:01
    File: 鼠标双击.py
Software: PyCharm
______________________________
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("http://www.baidu.com/")
driver.get("http://sahitest.com/demo/clicks.htm")
ele = driver.find_element(By.XPATH,"/html/body/form/input[2]")
# double_click双击
ActionChains(driver).double_click(ele).perform()

sleep(10)
