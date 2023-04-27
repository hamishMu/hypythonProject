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
import json
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


class TBGou:
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=option)

    def login(self):
        try:
            self.driver.get('https://login.taobao.com/member/login.jhtml')
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
            qrcode = self.driver.find_element(By.XPATH, '//*[@id="login"]/div[1]/i')
            if qrcode:
                qrcode.click()
            time.sleep(6)
            print("需要扫码")
            print("当前系统日期为:{}".format(datetime.datetime.now()))
            tb_cookies = self.driver.get_cookies()
            jsoncookies = json.dumps(tb_cookies)
            with open('tb_cookies', 'w') as f:
                f.write(jsoncookies)
            self.driver.get('https://cart.taobao.com/cart.htm')
            now = datetime.datetime.now()
            print('login success: ', now.strftime('%Y-%m-%d %H:%M:%S'))
        except Exception as e:
            print(e)

    def buyCart(self, times):
        try:

            while True:
                now = datetime.datetime.now()
                # 对比时间，时间到的话就点击结算
                if now >= times:
                    while True:
                        # 异常处理
                        try:
                            select_all = self.driver.find_element(By.XPATH, '//*[@id="J_SelectAll1"]')
                            if select_all:
                                select_all.click()
                                break
                        except Exception as e:
                            print(e)
                            print("找不到全选按钮....")
                            break
                # 点击结算按钮
                while True:
                    try:
                        # // *[ @ id = "J_FloatBar"] / div[2] / div[3] / div[5]
                        jiesuan = self.driver.find_element(By.ID, 'J_Go')
                        if jiesuan:
                            jiesuan.click()

                    except Exception as e:
                        print(e)
                        break
                # 提交订单
                while True:
                    try:
                        submit = self.driver.find_element(By.LINK_TEXT, '提交订单')
                        if submit:
                            submit.click()
                            now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                            print('抢购成功时间：%s' % now1)
                            break
                    except:
                        print('找不到提交订单...')
                        break
                # 支付
                while True:
                    try:
                        pad = self.driver.find_element(By.XPATH, '//*[@id="payPassword_rsainput"]')
                        if pad:
                            pad.send_keys('909356')
                            now2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                            print('抢购成功时间：%s' % now2)
                            break
                    except:
                        print('支付失败...')
        except Exception as e:
            print(e)
        finally:
            self.driver.quit()


if __name__ == '__main__':
    tb = TBGou()
    tb.login()
    qg_time = '2023-04-08 00:47:00'
    qg_date = datetime.datetime.strptime(qg_time, '%Y-%m-%d %H:%M:%S')
    tb.buyCart(qg_date)
