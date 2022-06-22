# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 20:39
# @Author  : yuchen
# @File    : fund.py
# @Software: PyCharm

from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask import request
from api.utils import paging_query
from models.fund import FundModel


class FundResource(Resource):
    @jwt_required()
    def get(self):
        """
        获取资金信息
        :param f_id:
        :return:
        """

        # 查询指定基金
        f_id = request.args.get("f_id", None)
        if f_id is not None:
            fund = FundModel.find_by_id(f_id)
            if not fund:
                return {"code": 0, "msg": "invalid fund id"}, 200
            return {"code": 1, "msg": "success", "data": {"fund": fund.json()}}, 200

        # 分页查询所有基金
        page_index = request.args.get("page_index", 1)
        page_size = request.args.get("page_size", 10)

        res, current_page, total_page, total_count = paging_query(FundModel, int(page_index), int(page_size))

        return {"code": 1, "msg": "success",
                "data": {"fund_list": [x.json() for x in res], "current_page": current_page, "total_page": total_page,
                         "total_count": total_count}}, 200
