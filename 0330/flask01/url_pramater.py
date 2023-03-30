# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/30 11:44
    File: url_pramater.py
Software: PyCharm
______________________________
"""

from flask import Flask

app = Flask(__name__)


# 定义路由
@app.route("/user")
def hello_world():
    return '这是url传参演示'


@app.route('/user/<name>')
def url_parameter(name):
    return "接受到的名称为： %s" % name


@app.route('/news/<int:id>')
def list_news(id):
    print(type(id))
    return "接受到的id为 %s"%id


if __name__ == '__main__':
    app.run(debug=True)
