# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 23:18
# @Author  : yuchen
# @File    : asset.py
# @Software: PyCharm

from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask import request
from models.asset import AssetModel
from datetime import datetime
from api.utils import get_product_info


class AssetResource(Resource):
    @jwt_required()
    def get(self):
        """
        获取资产信息
        :param a_id:
        :return:
        """

        a_id = request.args.get("a_id", None)
        if not a_id:
            return {"code": 0, "msg": "asset id can not be null"}, 400

        asset = AssetModel.find_by_id(a_id)
        if not asset:
            return {"code": 0, "msg": "invalid asset id"}, 400

        return {"code": 1, "msg": "success", "data": {"asset": asset.json()}}, 200

    @jwt_required()
    def post(self):
        """
        添加资产信息
        :return:
        """
        data = request.json
        a_product_id = data.get("a_product_id", None)
        a_product_type = data.get("a_product_type", None)
        a_number = data.get("a_number", 1)
        a_user_id = data.get("a_user_id", None)
        a_time = data.get("a_time", datetime.now().strftime("%Y-%m-%d-%H %H:%M:%S"))

        if a_product_id is None or a_product_type is None or a_number is None or a_user_id is None:
            return {"code": 0, "msg": "asset product id or product type or number or user id can not be null"}, 400

        # 如果不是本人或者管理员，则返回401
        if a_user_id != get_jwt_identity() and get_jwt()["user_type"] != 1:
            return {"code": 0, "msg": "permission denied"}, 401

        asset = AssetModel.query.filter(AssetModel.a_user_id == a_user_id, AssetModel.a_product_id == a_product_id,
                                        AssetModel.a_product_type == a_product_type).first()

        # 如果已经存在，则更新数量,时间
        if asset:
            asset.a_number += a_number
            asset.a_time = a_time
            asset.save_to_db()
            return {"code": 1, "msg": "success", "data": {"asset": asset.json()}}, 200

        # 如果不存在，则添加新的资产
        # 先判断要添加的资产是否存在
        asset_product = get_product_info(a_product_id, a_product_type)
        if not asset_product:
            return {"code": 0, "msg": "invalid asset product id or product type"}, 400
        asset = AssetModel(a_product_id=a_product_id, a_product_type=a_product_type, a_number=a_number,
                           a_user_id=a_user_id, a_time=a_time, a_state=1, a_profit=0)
        asset.save_to_db()
        return {"code": 1, "msg": "success", "data": {"asset": asset.json()}}, 201
