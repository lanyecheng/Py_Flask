#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/10

from flask import Flask, render_template
from flask import escape, url_for

app = Flask(__name__)

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def hello():
    return render_template('index.html', name=name, movies=movies)


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
