# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 14:23
# @Author  : yuchen
# @File    : financial_product.py
# @Software: PyCharm

from extensions import db


class FinancialProductModel(db.Model):
    """
    理财产品
    """
    __tablename__ = "financial_product"
    fp_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="理财产品ID")
    fp_code = db.Column(db.String(40), unique=True, nullable=False, index=True, comment="产品编码")
    fp_name = db.Column(db.String(40), nullable=False, comment="产品名称")
    fp_detail = db.Column(db.String(40), nullable=False, comment="产品描述")
    fp_time = db.Column(db.String(40), nullable=False, comment="理财年限")
    fp_amount = db.Column(db.Numeric(40, 8), nullable=False, default=0, comment="产品金额")



