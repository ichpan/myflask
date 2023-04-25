#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import logging

from flask import request, g, jsonify
from flask_jwt_extended import create_access_token, verify_jwt_in_request

from application.extensions import db, bcrypt
from application.apps.user import user_blueprint
from application.apps.user.model import User


@user_blueprint.route("/register", methods=['post'])
def register():
    data = request.get_json()
    username = data.get('username', None)
    password1 = data.get('password1', None)
    password2 = data.get('password2', None)
    mobile = data.get('mobile', None)

    if None in [username, password1, password2, mobile]:
        return jsonify(msg='请填写完整注册信息', code=4001), 400

    if len(password1) < 8:
        return jsonify(msg='密码长度至少8位', code=4002), 400

    if password1 != password2:
        return jsonify(msg='两次密码不一致', code=4003), 400

    if not re.match(r'^1[3-9]\d{9}$', mobile):
        return jsonify(msg='手机号格式不正确', code=4004), 400

    if User.query.filter_by(username=username).first():
        return jsonify(msg='用户名已存在', code=4005), 400

    password = bcrypt.generate_password_hash(password2)
    user = User(username=username, password=password, mobile=mobile)
    db.session.add(user)

    return jsonify(msg='注册成功', code=2000), 200


@user_blueprint.route("/login", methods=['post'])
def login():
    data = request.get_json()
    username = data.get('username', None)

    # check password
    password = data.get('password', None)
    if None in [username, password]:
        return jsonify(msg='用户信息不能为空', code=4006), 400

    if password is None or len(password) < 8:
        return jsonify(msg='密码长度至少8位', code=4002), 400

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        _claims = {"auther": "myflask"}
        access_token = create_access_token(username, additional_claims=_claims)
        return jsonify(code=2000, uid=user.id, username=user.username, access_token=access_token), 200
    else:
        return jsonify(code=4007, data=None, msg='Login failure'), 400


@user_blueprint.route("/userinfo", methods=['post'])
def userinfo():
    """
    获取用户信息列表
    """
    print(g.auther)
    query_obj = db.session.query(User).all()
    return jsonify(data=[query.as_dict() for query in query_obj]), 200
