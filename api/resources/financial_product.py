# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 22:00
# @Author  : yuchen
# @File    : financial_product.py
# @Software: PyCharm

from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask import request
from api.utils import paging_query
from models.financial_product import FinancialProductModel


class FinancialProductResource(Resource):
    @jwt_required()
    def get(self):
        """
        获取理财产品信息
        :param fp_id:
        :return:
        """

        # 查询指定理财产品
        fp_id = request.args.get("fp_id", None)
        if fp_id is not None:
            financial_product = FinancialProductModel.find_by_id(fp_id)
            if not financial_product:
                return {"code": 0, "msg": "invalid financial product id"}, 200
            return {"code": 1, "msg": "success", "data": {"financial_product": financial_product.json()}}, 200

        # 分页查询所有理财产品
        page_index = request.args.get("page_index", 1)
        page_size = request.args.get("page_size", 10)

        res, current_page, total_page, total_count = paging_query(FinancialProductModel, int(page_index),
                                                                  int(page_size))

        return {"code": 1, "msg": "success",
                "data": {"financial_product_list": [x.json() for x in res], "current_page": current_page,
                         "total_page": total_page, "total_count": total_count}}, 200
