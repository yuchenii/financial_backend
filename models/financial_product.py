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

    def __init__(self, fp_code, fp_name, fp_detail, fp_time, fp_amount):
        self.fp_code = fp_code
        self.fp_name = fp_name
        self.fp_detail = fp_detail
        self.fp_time = fp_time
        self.fp_amount = fp_amount

    def json(self):
        return {
            "fp_id": self.fp_id,
            "fp_code": self.fp_code,
            "fp_name": self.fp_name,
            "fp_detail": self.fp_detail,
            "fp_time": self.fp_time,
            "fp_amount": str(self.fp_amount)
        }

    @classmethod
    def find_by_id(cls, fp_id):
        return cls.query.filter_by(fp_id=fp_id).first()

    @classmethod
    def find_by_code(cls, fp_code):
        return cls.query.filter_by(fp_code=fp_code).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
