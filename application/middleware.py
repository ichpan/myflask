#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import request, g, abort
from flask_jwt_extended import verify_jwt_in_request

whitelist_routes = (
    '/api/v1/login',
    '/api/v1/register'
)


def before_request():
    if request.path not in whitelist_routes:
        try:
            _, jwt_data = verify_jwt_in_request()
            g.auther = jwt_data.get('auther')
        except Exception as err:
            abort(401, err.args[0])


def after_request(response):
    return response


def teardown_request(exception=None):
    pass
