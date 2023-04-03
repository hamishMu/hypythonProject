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
driver.get("http://sahitest.com/demo/mouseover.htm")
ele = driver.find_element(By.XPATH,"/html/body/form/input[1]")
ActionChains(driver).move_to_element(ele).perform()

sleep(10)

driver.quit()