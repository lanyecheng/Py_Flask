#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/10

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'
