# -*- coding: utf-8 -*-
"""
______________________________
  Author: muhuiyuan
  Email : muhuiyuan@foxmail.com
   Time : 2023/4/4 15:50
    File: app.py
Software: PyCharm
______________________________
"""
"""
登录接口，查询数据库
"""
from flask import Flask, render_template, request
import pymysql
import yaml

app = Flask(__name__)


def read(path):
    with open(path, 'r') as file:
        data = file.read()
        # result = yaml.load(data)
        result = yaml.load(data, Loader=yaml.FullLoader)
        return result


@app.route('/')
def index():
    return render_template('login.html')


@app.route("/login", methods=['POST','GET'])
def login():
    form_data = request.form
    username = form_data.get('username')
    print(username, type(username))
    password = form_data.get("password")
    print(password, type(password))
    file_name = 'database.yaml'
    result_db = read(file_name)
    db = pymysql.connect(**result_db)
    print("db->", db)
    cursor = db.cursor()
    try:
        sql = 'select * from user where username = "{0}" and password = "{1}" '.format(username, password)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is not None:
            message = "登录成功"
            print(result)
            print("登录成功")
            return render_template("index.html", message=message)
        else:
            message = "用户名或者密码错误！请重新登录"
            print("用户名或者密码错误！请重新登录")
            return render_template('login.html', message=message)
    except Exception as e:
        message = "用户名或者密码错误！请重新登录"
        db.rollback()
        print(e)
        return render_template("login.html", message=message)
    finally:
        cursor.close()
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
