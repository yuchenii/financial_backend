# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 13:15
# @Author  : yuchen
# @File    : user.py
# @Software: PyCharm
from sqlalchemy import null

from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):
    """
    用户表
    """
    __tablename__ = "user"
    u_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="用户ID")
    u_name = db.Column(db.String(40), nullable=False, comment="用户名")
    u_phone = db.Column(db.String(40), unique=True, nullable=False, index=True, comment="用户手机号")
    u_email = db.Column(db.String(40), unique=True, nullable=False, index=True, comment="用户邮箱")
    u_password = db.Column(db.String(128), nullable=False, comment="用户密码")
    u_type = db.Column(db.Integer, nullable=False, default=0, comment="用户类型 0:用户 1：管理员")

    bank_card_info = db.relationship("BankCardModel", back_populates="user", lazy='dynamic')
    asset_info = db.relationship("AssetModel", back_populates="user", lazy='dynamic')
    token_info = db.relationship("TokenModel", back_populates="user", lazy='dynamic')

    def __init__(self, u_name, u_phone, u_email, u_password, u_type):
        self.u_name = u_name
        self.u_phone = u_phone
        self.u_email = u_email
        self.u_password = u_password
        self.u_type = u_type

    def json(self):
        return {
            "u_id": self.u_id,
            "u_name": self.u_name,
            "u_phone": self.u_phone,
            "u_email": self.u_email,
            "u_type": self.u_type
        }

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(u_id=user_id).first()

    @classmethod
    def find_by_user_name(cls, user_name):
        return cls.query.filter_by(u_name=user_name).first()

    @classmethod
    def find_by_user_email(cls, user_email):
        return cls.query.filter_by(u_email=user_email).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_asset_list_by_user_id(cls, user_id):
        return cls.query.filter_by(u_id=user_id).first().asset_info.all()

    @classmethod
    def find_bank_card_list_by_user_id(cls, user_id):
        return cls.query.filter_by(u_id=user_id).first().bank_card_info.all()

    def set_password(self, password):
        self.u_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.u_password, password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
