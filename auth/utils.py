# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 11:48
# @Author  : yuchen
# @File    : utils.py
# @Software: PyCharm

from datetime import datetime

from flask_jwt_extended import decode_token
from sqlalchemy.orm.exc import NoResultFound

from extensions import db
from models.token import TokenModel


def save_token_to_db(encoded_token, identity_claim):
    """
    往数据库里增加一个token
    :param encoded_token:
    :param identity_claim:
    """
    decoded_token = decode_token(encoded_token)

    t_jti = decoded_token["jti"]
    t_type = decoded_token["type"]
    t_user_id = decoded_token[identity_claim]
    t_expires = datetime.fromtimestamp(decoded_token["exp"])
    t_revoked = False

    db_token = TokenModel(
        t_jti=t_jti,
        t_type=t_type,
        t_user_id=t_user_id,
        t_expires=t_expires,
        t_revoked=t_revoked,
    )
    db.session.add(db_token)
    db.session.commit()


def is_token_revoked(decoded_token):
    """
    检查token是否过期了
    """
    t_jti = decoded_token["jti"]
    try:
        token = TokenModel.query.filter_by(t_jti=t_jti).one()
        return token.t_revoked
    except NoResultFound:
        return True


def revoke_token(token_jti, t_user_id: int):
    """
    把token设置成过期
    """
    try:
        token = TokenModel.query.filter_by(t_jti=token_jti, t_user_id=t_user_id).one()
        token.t_revoked = True
        db.session.commit()
    except NoResultFound:
        raise Exception("Could not find the token {}".format(token_jti))


class UserIdentity(object):
    """
    用户认证信息
    """
    def __init__(self, user_id: int, user_type: int):
        self.user_id = user_id
        self.user_type = user_type
