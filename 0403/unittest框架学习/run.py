# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/3 23:19
    File: run.py
Software: PyCharm
______________________________
"""
import time

"""
通过使用HTMLTestRunner模块生成测试报告
"""
import unittest
from XTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 查找当前目录的测试用例文件
    testSuite = unittest.TestLoader().discover('.')
    file_name = "d:/test_{}.html".format(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
    with open(file_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='这里是报告的标题', description='这里是报告的描述信息', language='en',
                                rerun=3)
        runner.run(testSuite)
