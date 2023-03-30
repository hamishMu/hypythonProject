# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/3/30 11:34
    File: index.py
Software: PyCharm
______________________________
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
