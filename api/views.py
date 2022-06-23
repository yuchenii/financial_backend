# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 9:14
# @Author  : yuchen
# @File    : views.py
# @Software: PyCharm

from flask import Blueprint, current_app, jsonify
from flask_restful import Api

from api.resources.user import UserResource, UserListResource, UserAssetListResource, UserBankCardListResource
from api.resources.bank_card import BankCardResource
from api.resources.fund import FundResource
from api.resources.financial_product import FinancialProductResource
from api.resources.insurance import InsuranceResource
from api.resources.asset import AssetResource

apiv1_bp = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(apiv1_bp)

api.add_resource(UserResource, "/user")
api.add_resource(UserListResource, "/user/all")  # 管理员查询所有用户
api.add_resource(UserAssetListResource, "/user/asset")  # 用户查询自己的资产
api.add_resource(UserBankCardListResource, "/user/bank_card")  # 用户查询自己的银行卡
api.add_resource(BankCardResource, "/bank_card")  # 银行卡CURD
api.add_resource(FundResource, "/fund")  # 资金CURD
api.add_resource(FinancialProductResource, "/financial_product")  # 理财产品CURD
api.add_resource(InsuranceResource, "/insurance")  # 保险产品CURD
api.add_resource(AssetResource, "/asset")  # 资产CURD
