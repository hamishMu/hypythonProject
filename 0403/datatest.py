# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/3 10:53
    File: datatest.py
Software: PyCharm
______________________________
"""
from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
html_file = 'File:///'+os.getcwd()+os.sep+"myhtml.html"
driver.get(html_file)
sleep(2)
driver.find_element(By.TAG_NAME,'input').send_keys("002023/04/03")