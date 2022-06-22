# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 14:49
# @Author  : yuchen
# @File    : fund.py
# @Software: PyCharm

from extensions import db

class FundModel(db.Model):
    """
    基金表
    """
    __tablename__ = "fund"
    f_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="基金ID")
    f_code = db.Column(db.String(40), unique=True, nullable=False, index=True, comment="基金编码")
    f_name = db.Column(db.String(40), nullable=False, comment="基金名称")
    f_type = db.Column(db.String(40), nullable=False, comment="基金类型")
    f_risk_level = db.Column(db.String(40), nullable=False, comment="风险等级")
    f_administrator = db.Column(db.String(40), nullable=False, comment="基金管理人")
    f_amount = db.Column(db.Numeric(40, 8), nullable=False, default=0, comment="基金金额")



