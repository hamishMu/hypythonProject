# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/7 23:17
    File: test_case_demo02.py
Software: PyCharm

包含函数定义的测试用例test_c,又包含class中的测试用例test_a,test_b.

______________________________
"""

import pytest


def test_c():
    print('ccccc')
    assert 'c' == 'c'


class Test01:
    def test_a(self):
        print('aaaaa')
        assert 'a' == 'a'

    def test_b(self):
        print('bbbb')
        assert 'b' == 'b'

"""
pytest.main['-s']执行当前文件所在目录下所有符合条件的测试用例。
"""
if __name__ == '__main__':
    # 在class风格的脚本中，调试时候可以通过文件名后加冒号和class名来指定某个class.
    # pytest.main['-s', 'test_case_demo02.py::Test01
    # pytest.main(['-s', 'test_case_demo02.py'])
    pytest.main(['-s', './test_case_demo02.py::Test01'])
