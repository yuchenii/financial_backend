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


class UserResource(Resource):
    @jwt_required()
    def get(self):
        """
        获取用户信息
        :param user_id:
        :return:
        """
        user_id = request.args.get("user_id", None)
        if not user_id:
            return {"code": 0, "msg": "user id can not be null"}, 400

        user_info = UserModel.find_by_user_id(user_id)

        if not user_info:
            return {"code": 0, "msg": "invalid user id"}, 200

        # 如果不是本人或者管理员，则返回401
        if user_info.u_id != get_jwt_identity() and get_jwt()["user_type"] != 1:
            return {"code": 0, "msg": "permission denied"}, 401

        return {
            "code": 1,
            "msg": "success",
            "data": user_info.json()
        }

    def post(self):
        """
        添加用户信息
        :return:
        """
        data = request.get_json()
        user_name = data.get("user_name", None)
        user_phone = data.get("user_phone", None)
        user_email = data.get("user_email", None)
        user_password = data.get("user_password", None)
        user_type = data.get("user_type", 0)

        if user_name is None or user_phone is None or user_email is None or user_password is None:
            return {"code": 0, "msg": "user name or user phone or user email or user password can not be null"}, 400

        if UserModel.find_by_user_email(user_email):
            return {"code": 0, "msg": "user email already exists"}, 400

        user = UserModel(u_name=user_name, u_phone=user_phone, u_email=user_email, u_password=user_password, u_type=0)
        user.set_password(user_password)

        try:
            user.save_to_db()
        except:
            return {"code": 0, "msg": "usr phone already exists"}, 400

        return {"code": 1, "msg": "success", "data": user.json()}, 201


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
