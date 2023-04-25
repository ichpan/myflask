#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS

from application.settings.dev import DevConfig
from application.settings.prod import ProdConfig
from application.extensions import db, redis_cli, bcrypt, jwt
from application.logger import setup_log
from application.middleware import before_request, after_request, teardown_request
from application.apps.index import index_blueprint
from application.apps.user import user_blueprint

config = {
    "dev": DevConfig,
    "prod": ProdConfig,
}


def create_app(conf_name):
    app = Flask(__name__)
    conf = config[conf_name]

    # loading config.
    app.config.from_object(conf)

    # cross-domain
    CORS(app)

    # password tools
    bcrypt.init_app(app)

    # open CSRF
    # CSRFProtect(app)

    # config db
    db.init_app(app)

    # config redis
    redis_cli.init_app(app)

    # config logger
    setup_log(conf)

    # json web token.
    jwt.init_app(app)

    # middleware
    app.before_request(before_request)
    app.after_request(after_request)
    app.teardown_request(teardown_request)

    # blueprint
    app.register_blueprint(index_blueprint, url_prefix='/api/v1')
    app.register_blueprint(user_blueprint, url_prefix='/api/v1')

    return app
