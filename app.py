# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 10:11
# @Author  : yuchen
# @File    : extensions.py
# @Software: PyCharm

from flask import Flask
from extensions import db, jwt, cors
from auth.views import auth_bp
from api.views import apiv1_bp
from config import config
import os


def create_app(config_name=None):
    """
    创建app
    :param config_name:
    :return: app
    """
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('financial_backend')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_request_handlers(app)

    return app


def register_extensions(app):
    """
    注册插件
    :param app:
    :return:
    """
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)


def register_blueprints(app):
    """
    注册蓝本
    :param app:
    :return:
    """
    app.register_blueprint(auth_bp)
    app.register_blueprint(apiv1_bp)


def register_request_handlers(app):
    """
    注册请求处理
    :param app:
    :return:
    """

    @app.before_first_request
    def create_tables():
        """
        创建数据库表
        :return:
        """

        from models.user import UserModel
        from models.bank_card import BankCardModel
        from models.financial_product import FinancialProductModel
        from models.fund import FundModel
        from models.insurance import InsuranceModel
        from models.asset import AssetModel
        from models.token import TokenModel

        db.create_all()