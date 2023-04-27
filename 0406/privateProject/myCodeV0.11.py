# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/6 21:47
    File: myCodeV0.1.py
Software: PyCharm
______________________________
"""
from selenium import webdriver
import datetime, time

from selenium.webdriver.common.by import By


def login():

    # 打开淘宝登录页，并经行扫码登录
    brower.get("https://login.taobao.com/member/login.jhtml")

    # 等待selenium 框架加载网页完成
    brower.implicitly_wait(3)

    if brower.find_element(By.XPATH,'//*[@id="login"]/div[1]/i'):
        brower.find_element(By.XPATH, '//*[@id="login"]/div[1]/i').click()

        brower.get("https://cart.taobao.com/cart.htm")
    brower.implicitly_wait(3)

    now = datetime.datetime.now()
    print('login success: ', now.strftime('%Y-%m-%d %H:%M:%S'))


# 2. 实现商品购买
def buy(times):
    # 点击购物车里的全选按钮
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now > times:
            while True:
                # 异常处理
                try:
                    if brower.find_element_by_id("J_SelectAll2"):
                        brower.find_element_by_id("J_SelectAll2").click()
                        break
                except:
                    print('找不到全选按钮...')

            # 点击结算按钮//*[@id="J_Go"]/span
            while True:
                try:
                    if brower.find_element_by_xpath('//*[@id="J_Go"]/span'):
                        brower.find_element_by_xpath('//*[@id="J_Go"]/span').click()
                        print('结算成功')
                        break
                except:
                    print('找不到结算按钮')

            # 提交订单
            # while True:
            #     try:
            #         if brower.find_element_by_link_text('提交订单'):
            #             brower.find_element_by_link_text("提交订单").click()
            #             now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            #             print('抢购成功时间：%s' % now1)
            #             break
            #     except:
            #         print('我的银行卡没钱...')
            #
            # time.sleep(0.01)#2019-06-09 17:05:00.000000


# 启动函数2019-11-02 14:03:00.000000


if __name__ == "__main__":
    # 2023-04-06 23:41:31.184316
    times = input("请输入抢购时间，格式(2019-05-08 20:00:00.000000)：")
    brower = webdriver.Chrome()
    login()
    buy(times)
