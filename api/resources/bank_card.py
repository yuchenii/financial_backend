# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 15:23
# @Author  : yuchen
# @File    : bank_card.py
# @Software: PyCharm
import json

from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask import request
from models.bank_card import BankCardModel


class BankCardResource(Resource):
    @jwt_required()
    def get(self):
        """
        获取银行卡信息
        :param bc_id:
        :return:
        """
        bc_id = request.args.get("bc_id", None)
        if not bc_id:
            return {"code": 0, "msg": "bank card id can not be null"}, 400

        bank_card_info = BankCardModel.find_by_id(bc_id)

        if not bank_card_info:
            return {"code": 0, "msg": "invalid bank card id"}, 200

        # 如果不是本人或者管理员，则返回401
        if bank_card_info.bc_user_id != get_jwt_identity() and get_jwt()["user_type"] != 1:
            return {"code": 0, "msg": "permission denied"}, 401

        return {
            "code": 1,
            "msg": "success",
            "data": bank_card_info.json()
        }

    @jwt_required()
    def post(self):
        """
        添加银行卡信息
        :return:
        """
        data = request.get_json()
        bc_id = data.get("bc_id", None)
        bc_user_id = data.get("bc_user_id", None)
        bc_type = data.get("bc_type", 0)

        if bc_id is None or bc_user_id is None:
            return {"code": 0, "msg": "bank card id or user id can not be null"}, 400

        # 如果不是本人或者管理员，则返回401
        if bc_user_id != get_jwt_identity() and get_jwt()["user_type"] != 1:
            return {"code": 0, "msg": "permission denied"}, 401

        if BankCardModel.find_by_id(bc_id):
            return {"code": 0, "msg": "bank card id already exists"}, 400

        bank_card_info = BankCardModel(bc_id=bc_id, bc_user_id=bc_user_id, bc_type=bc_type, bc_amount=0)

        try:
            bank_card_info.save_to_db()
        except:
            return {"code": 0, "msg": "invalid bc_user_id"}, 400

        return {"code": 1, "msg": "success", "data": bank_card_info.json()}, 201

    @jwt_required()
    def put(self):
        """
        更新银行卡信息
        :return:
        """
        data = request.json
        bc_id = data.get("bc_id", None)
        bc_amount = data.get("bc_amount", None)

        if bc_id is None or bc_amount is None:
            return {"code": 0, "msg": "bank card id or amount can not be null"}, 400

        bank_card = BankCardModel.find_by_id(bc_id)

        if not bank_card:
            return {"code": 0, "msg": "invalid bank card id"}, 400

        # 如果不是本人或者管理员，则返回401
        if bank_card.bc_user_id != get_jwt_identity() and get_jwt()["user_type"] != 1:
            return {"code": 0, "msg": "permission denied"}, 401

        bank_card.bc_amount = bc_amount
        bank_card.save_to_db()

        return {"code": 1, "msg": "success", "data": bank_card.json()}, 200
