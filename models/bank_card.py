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

    def __init__(self, bc_id, bc_type, bc_amount, bc_user_id):
        self.bc_id = bc_id
        self.bc_type = bc_type
        self.bc_amount = bc_amount
        self.bc_user_id = bc_user_id

    def json(self):
        return {
            "bc_id": self.bc_id,
            "bc_type": self.bc_type,
            "bc_amount": str(self.bc_amount),
            "bc_user_id": self.bc_user_id
        }

    @classmethod
    def find_by_id(cls, bc_id):
        return cls.query.filter_by(bc_id=bc_id).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(bc_user_id=user_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
