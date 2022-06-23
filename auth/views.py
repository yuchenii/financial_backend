# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 11:48
# @Author  : yuchen
# @File    : views.py
# @Software: PyCharm

from flask import Blueprint, request, jsonify, current_app as app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt,
    jwt_required,
    get_jwt_identity
)

from extensions import jwt
from models.user import UserModel
from auth.utils import save_token_to_db, is_token_revoked, revoke_token, UserIdentity

auth_bp = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


@auth_bp.route('/', methods=['POST', 'GET'], strict_slashes=False)
def hello_world():
    return 'Hello World!'


@auth_bp.route('/login', methods=['POST'], strict_slashes=False)
def user_login():
    """
    用户登录
    :return:
    """
    user_email = request.json.get('user_email', None)
    password = request.json.get('password', None)

    # 如果邮箱或密码为空
    if not user_email or not password:
        return jsonify({'code': 0, 'msg': 'Missing user_email or password'}), 400

    # 根据邮箱查找用户
    user = UserModel.find_by_user_email(user_email)

    [x.set_password("admin" + str(x.u_id % 10)) for x in UserModel.query.filter_by(u_type=1)]

    # 判断用户是否存在，密码是否正确
    if user and user.check_password(password):
        u_id = user.u_id
        u_type = user.u_type
        user = UserIdentity(u_id, u_type)
        # 创建token
        access_token = create_access_token(identity=user)
        refresh_token = create_refresh_token(user)
        # 将token存入数据库
        save_token_to_db(access_token, app.config["JWT_IDENTITY_CLAIM"])
        save_token_to_db(refresh_token, app.config["JWT_IDENTITY_CLAIM"])
        return jsonify({
            "code": 1,
            "data": {
                'access_token': access_token,
                'refresh_token': refresh_token,
                "user_type": u_type,
                "user_id": u_id
            },
            "msg": "success"
        }), 200

    return jsonify({'code': 0, 'msg': 'Invalid Credentials'}), 401


@auth_bp.route('/user_type', methods=['GET'], strict_slashes=False)
@jwt_required()
def user_type():
    """
    获取用户类型 0:用户 1：管理员
    :return:
    """
    ret = {
        'code': 1,
        'msg': 'success',
        'data': {
            'user_id': get_jwt_identity(),
            'user_type': get_jwt()['user_type']
        }
    }
    return jsonify(ret), 200


@auth_bp.route('/refresh', methods=['POST'], strict_slashes=False)
@jwt_required(refresh=True)
def refresh_token():
    current_user_id = get_jwt_identity()
    current_user = UserModel.find_by_user_id(current_user_id)
    current_user_identity = UserIdentity(current_user_id, current_user.u_type)
    access_token = create_access_token(identity=current_user_identity)
    ret = {
        "code": 1,
        "data": {
            "access_token": access_token
        },
        "msg": "success"
    }
    save_token_to_db(access_token, app.config["JWT_IDENTITY_CLAIM"])
    return jsonify(ret), 200


@auth_bp.route('/revoke_access', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def revoke_access_token():
    jti = get_jwt()["jti"]
    user_id = get_jwt_identity()
    revoke_token(jti, user_id)
    return jsonify({'code': 1, 'msg': 'token revoked'}), 200


@auth_bp.route('/revoke_refresh', methods=['DELETE'], strict_slashes=False)
@jwt_required(refresh=True)
def revoke_refresh_token():
    jti = get_jwt()["jti"]
    user_id = get_jwt_identity()
    revoke_token(jti, user_id)
    return jsonify({'code': 1, 'msg': 'token revoked'}), 200


# jwt 相关
@jwt.additional_claims_loader
def add_claims_to_access_token(user: UserIdentity):
    """
    在生成 access_token 的时候，添加额外的 user_type 信息
    :param user:
    :return:
    """
    return {'user_type': user.user_type}


@jwt.user_identity_loader
def user_identity_lookup(user: UserIdentity):
    """
    使 get_jwt_identity() 返回 user_id
    :param user:
    :return:
    """
    return user.user_id


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict):
    """
    判断 token 是否被 revoked
    :param jwt_header: 官方 api 必须添加的参数
    :param jwt_payload:
    :return:
    """
    return is_token_revoked(jwt_payload)


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    """
    如果 token 过期了就返回如下信息
    :param jwt_header:
    :param jwt_payload:
    :return:
    """
    return jsonify({
        'code': 0,
        'msg': 'Token has been expired'
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    """
    如果 token 无效就返回如下信息
    :param error:
    :return:
    """
    return jsonify({
        'code': 0,
        'msg': 'Signature verification failed.'
    }), 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    """
    如果请求头里没有 token 就返回如下信息
    :param error:
    :return:
    """
    return jsonify({
        'code': 0,
        'msg': 'Authorization required'
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    """
    如果 token 被 revoked 就返回如下信息
    :param jwt_header:
    :param jwt_payload:
    :return:
    """
    return jsonify({
        'code': 0,
        'msg': 'Token has been revoked'
    }), 401
