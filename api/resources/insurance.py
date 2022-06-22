# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 22:39
# @Author  : yuchen
# @File    : insurance.py
# @Software: PyCharm

from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask import request
from api.utils import paging_query
from models.insurance import InsuranceModel


class InsuranceResource(Resource):
    @jwt_required()
    def get(self):
        """
        获取保险信息
        :param i_id:
        :return:
        """

        # 查询指定保险
        i_id = request.args.get("i_id", None)
        if i_id is not None:
            insurance = InsuranceModel.find_by_id(i_id)
            if not insurance:
                return {"code": 0, "msg": "invalid insurance id"}, 200
            return {"code": 1, "msg": "success", "data": {"insurance": insurance.json()}}, 200

        # 分页查询所有保险
        page_index = request.args.get("page_index", 1)
        page_size = request.args.get("page_size", 10)

        res, current_page, total_page, total_count = paging_query(InsuranceModel, int(page_index), int(page_size))

        return {"code": 1, "msg": "success",
                "data": {"insurance_list": [x.json() for x in res], "current_page": current_page,
                         "total_page": total_page, "total_count": total_count}}, 200

