# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 15:12
# @Author  : yuchen
# @File    : asset.py
# @Software: PyCharm

from extensions import db
from api.utils import get_product_info


class AssetModel(db.Model):
    """
    资产表
    """
    __tablename__ = "asset"
    a_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="资产ID")
    a_product_id = db.Column(db.Integer, nullable=False, index=True, comment="产品ID")
    a_product_type = db.Column(db.Integer, nullable=False, comment="产品类型 0:理财产品 1:保险 2:基金")
    a_state = db.Column(db.Integer, nullable=False, default=1, comment="资产状态 0:冻结 1:可用")
    a_number = db.Column(db.Integer, nullable=False, default=1, comment="资产数量")
    a_time = db.Column(db.DateTime, nullable=False, comment="资产购买时间")
    a_profit = db.Column(db.Numeric(40, 8), nullable=False, default=0, comment="资产收益")

    a_user_id = db.Column(db.Integer, db.ForeignKey("user.u_id"), nullable=False, comment="用户ID")
    user = db.relationship("UserModel", back_populates="asset_info")

    def __init__(self, a_product_id, a_product_type, a_state, a_number, a_time, a_profit, a_user_id):
        self.a_product_id = a_product_id
        self.a_product_type = a_product_type
        self.a_state = a_state
        self.a_number = a_number
        self.a_time = a_time
        self.a_profit = a_profit
        self.a_user_id = a_user_id

    def json(self):
        return {
            "a_id": self.a_id,
            "a_product_type": self.a_product_type,
            "a_product_info": get_product_info(self.a_product_id, self.a_product_type),
            "a_state": self.a_state,
            "a_number": self.a_number,
            "a_time": str(self.a_time),
            "a_profit": str(self.a_profit),
            "a_user_id": self.a_user_id
        }

    @classmethod
    def find_by_id(cls, a_id):
        return cls.query.filter_by(a_id=a_id).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(a_user_id=user_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
