# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/7 20:23
    File: wmi_01.py
Software: PyCharm
使用wmi库获取机器的硬件信息
______________________________
"""
import wmi
# 获取cpu火序列号
m_wmi = wmi.WMI()
cpu_info = m_wmi.Win32_Processor()
if len(cpu_info) > 0:
    serial_number = cpu_info[0].ProcessorId
    print(serial_number)

