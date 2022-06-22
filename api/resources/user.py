# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 9:14
# @Author  : yuchen
# @File    : user.py
# @Software: PyCharm

from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask import request
from models.user import UserModel


class UserListResource(Resource):
    @jwt_required()
    def get(self):
        return {'code': 1,
                'msg': 'u_type 用户类型 0:用户 1：管理员',
                'data': {
                    'users': [user.json() for user in UserModel.find_all()]
                }
                }, 200


class UserAssetListResource(Resource):
    @jwt_required()
    def get(self):
        """
        获取用户资产列表
        :param user_id:
        :return:
        """
        user_id = request.args.get("user_id", None)
        if not user_id:
            return {"code": 0, "msg": "user id can not be null"}, 400

        user_id = int(user_id)

        # 如果不是本人或者管理员，则返回401
        if user_id != get_jwt_identity() and get_jwt()["user_type"] != 1:
            return {"code": 0, "msg": "permission denied"}, 401

        asset_list = UserModel.find_asset_list_by_user_id(user_id)
        if asset_list:
            return {"code": 1, "msg": "success", "data": {"asset_list": [x.json() for x in asset_list]}}, 200
        else:
            return {"code": 0, "msg": "no asset"}, 200


class UserBankCardListResource(Resource):
    @jwt_required()
    def get(self):
        """
        获取用户银行卡列表
        :param user_id:
        :return:
        """

        user_id = request.args.get("user_id", None)
        if not user_id:
            return {"code": 0, "msg": "user id can not be null"}, 400

        user_id = int(user_id)

        # 如果不是本人或者管理员，则返回401
        if user_id != get_jwt_identity() and get_jwt()["user_type"] != 1:
            return {"code": 0, "msg": "permission denied"}, 401

        bank_card_list = UserModel.find_bank_card_list_by_user_id(user_id)
        if bank_card_list:
            return {"code": 1, "msg": "success", "data": {"bank_card_list": [x.json() for x in bank_card_list]}}, 200
        else:
            return {"code": 0, "msg": "no bank card"}, 200
