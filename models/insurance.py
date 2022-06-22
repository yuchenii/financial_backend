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

    def __init__(self, i_code, i_name, i_people, i_time, i_item, i_amount):
        self.i_code = i_code
        self.i_name = i_name
        self.i_people = i_people
        self.i_time = i_time
        self.i_item = i_item
        self.i_amount = i_amount

    def json(self):
        return {
            "i_id": self.i_id,
            "i_code": self.i_code,
            "i_name": self.i_name,
            "i_people": self.i_people,
            "i_time": self.i_time,
            "i_item": self.i_item,
            "i_amount": str(self.i_amount)
        }

    @classmethod
    def find_by_id(cls, i_id):
        return cls.query.filter_by(i_id=i_id).first()

    @classmethod
    def find_by_code(cls, i_code):
        return cls.query.filter_by(i_code=i_code).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()