# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 13:58
# @Author  : yuchen
# @File    : bank_card.py
# @Software: PyCharm

from extensions import db


class BankCardModel(db.Model):
    """
    银行卡
    """
    __tablename__ = "bank_card"
    bc_id = db.Column(db.String(40), primary_key=True, comment="银行卡ID")
    bc_type = db.Column(db.Integer, nullable=False, default=0, comment="银行卡类型 0:储蓄卡 1:信用卡")
    bc_amount = db.Column(db.Numeric(40, 8), nullable=False, default=0, comment="银行卡金额")

    bc_user_id = db.Column(db.Integer, db.ForeignKey("user.u_id"), nullable=False, comment="用户ID")
    user = db.relationship("UserModel", back_populates="bank_card_info")

