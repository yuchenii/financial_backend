# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 13:11
# @Author  : yuchen
# @File    : token.py
# @Software: PyCharm

from extensions import db


class TokenModel(db.Model):
    """
    token表
    """
    __tablename__ = "token"
    t_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    t_jti = db.Column(db.String(40), unique=True, nullable=False, comment="jwt的唯一标识")
    t_type = db.Column(db.String(10), nullable=False, comment="token类型")
    t_revoked = db.Column(db.Boolean, nullable=False, default=False, comment="是否撤销")
    t_expires = db.Column(db.DateTime, nullable=False, comment="撤销时间")

    t_user_id = db.Column(db.Integer, db.ForeignKey("user.u_id"), nullable=False, comment="用户ID")
    user = db.relationship("UserModel", back_populates="token_info")

    def json(self):
        return {
            "t_id": self.t_id,
            "t_jti": self.t_jti,
            "t_type": self.t_type,
            "t_revoked": self.t_revoked,
            "t_expires": self.t_expires
        }

