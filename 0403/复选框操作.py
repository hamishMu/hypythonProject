# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/3 10:27
    File: 复选框操作.py
Software: PyCharm
______________________________
"""
from  selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/clicks.htm")

ele = driver.find_element("xpath",'/html/body/form/input[6]')
ele.click()
sleep(3)
if ele.is_selected():
    print("pass")
sleep(2)
ele.send_keys(Keys.SPACE)
sleep(3)
driver.quit()