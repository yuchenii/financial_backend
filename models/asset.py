# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 15:12
# @Author  : yuchen
# @File    : asset.py
# @Software: PyCharm

from extensions import db

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

