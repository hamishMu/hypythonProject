# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/3 19:44
    File: 将cookie存储到本地.py
Software: PyCharm
______________________________
"""

from selenium import webdriver
from time import sleep
import  json

from selenium.webdriver.common.by import By

"""
该文件用来保存cookie
"""

driver = webdriver.Chrome()
driver.maximize_window()
#
driver.get("https://www.zhihu.com/signin?next=%2F")
driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/div/div/div[2]/div/div[1]/div/div[1]/form/div[1]/div[2]').click()

sleep(3)

driver.find_element(By.NAME,'username').send_keys("731605632@qq.com")
driver.find_element(By.NAME,'password').send_keys("woaiwojia/1314")
driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/div/div/div[2]/div/div[1]/div/div[1]/form/button').click()

mycookies = driver.get_cookies()
jsoncookies = json.dumps(mycookies)
with open("mycookies.json",'w')as f:
    f.write(jsoncookies)

driver.quit()
