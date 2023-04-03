# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/3 22:37
    File: 无界面运行.py
Software: PyCharm
______________________________
"""
from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get("http://www.baidu.com")
sleep(3)
driver.quit()