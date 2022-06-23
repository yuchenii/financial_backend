# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 9:21
# @Author  : yuchen
# @File    : wsgi.py
# @Software: PyCharm

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from app import create_app

app = create_app('production')