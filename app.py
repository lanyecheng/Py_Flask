#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/10

from flask import Flask
from flask import escape, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'


@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)


@app.route('/test')
def test_url_for():
    # 下面是调用示例
    print(url_for('hello'))
    print(url_for('user_page', name='Bo bo'))
    print(url_for('user_page', name='Mr.zhang'))
    print(url_for('test_url_for'))
    # 下面这个调用传入多余的关键字参数，它们会作为查询字符串附加到 url 后面
    print(url_for('test_url_for', num=2))
    return 'Test Page'
