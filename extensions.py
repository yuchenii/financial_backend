# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 10:11
# @Author  : yuchen
# @File    : extensions.py
# @Software: PyCharm

from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()