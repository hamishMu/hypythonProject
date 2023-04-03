# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/3 22:05
    File: 读取cookies获取免登录效果.py
Software: PyCharm
______________________________
"""
from selenium import webdriver
import  time
import  json
from time import sleep

from selenium.webdriver.common.by import By

"""
通过导入cookies的的方式来实现登录，注意刷新页面
"""

driver = webdriver.Chrome()
driver.get("https://www.zhihu.com/signin?next=%2F")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/div/div/div[2]/div/div[1]/div/div[1]/form/div[1]/div[2]').click()

sleep(3)
cookies_file = 'mycookies.json'
with open(cookies_file,'r')as f:
    cookies_str = f.readline()
    cookies_dict = json.loads(cookies_str)

driver.delete_all_cookies()
for cookie in cookies_dict:
    for k in cookie.keys():
        if k=='expiry':
            cookie[k]=int(cookie[k])
print(cookie)
driver.add_cookie(cookie)

time.sleep(2)
driver.refresh()
sleep(20)

