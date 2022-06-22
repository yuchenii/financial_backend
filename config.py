# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 10:20
# @Author  : yuchen
# @File    : config.py.py
# @Software: PyCharm

import os


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECURE_KEY', 'secret_key')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://financial:financial@localhost/financial'
    PROPAGATE_EXCEPTIONS = True


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://financial:financial@localhost/financial'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql://financial:financial@localhost/financial')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}