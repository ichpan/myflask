#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_wtf.csrf import CSRFProtect

from application.settings.dev import DevConfig
from application.settings.prod import ProdConfig
from application import extensions, logger, middleware, error_handlers
from application.apps import index, user

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
    extensions.CORS(app)

    # password tools
    extensions.bcrypt.init_app(app)

    # open CSRF
    # CSRFProtect(app)

    # config db
    extensions.db.init_app(app)

    # config redis
    extensions.redis_cli.init_app(app)

    # config logger
    logger.setup_log(conf)

    # json web token.
    extensions.jwt.init_app(app)

    # middleware
    app.before_request(middleware.before_request)
    app.after_request(middleware.after_request)
    app.teardown_request(middleware.teardown_request)

    # error handles
    app.register_error_handler(404, error_handlers.exception_404_not_found)
    app.register_error_handler(405, error_handlers.exception_method_not_allow)

    # blueprint
    app.register_blueprint(index.index_blueprint, url_prefix='/api/v1')
    app.register_blueprint(user.user_blueprint, url_prefix='/api/v1')

    return app
