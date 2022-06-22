# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 14:41
# @Author  : yuchen
# @File    : insurance.py
# @Software: PyCharm

from extensions import db

class InsuranceModel(db.Model):
    """
    保险表
    """
    __tablename__ = "insurance"
    i_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="保险ID")
    i_code = db.Column(db.String(40), unique=True, nullable=False, index=True, comment="保险编码")
    i_name = db.Column(db.String(40), nullable=False, comment="保险名称")
    i_people = db.Column(db.String(40), nullable=False, comment="适用人群")
    i_time = db.Column(db.String(40), nullable=False, comment="保险年限")
    i_item = db.Column(db.String(40), nullable=False, comment="保险项目")
    i_amount = db.Column(db.Numeric(40, 8), nullable=False, default=0, comment="保险金额")