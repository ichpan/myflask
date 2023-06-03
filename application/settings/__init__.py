#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

BaseDir = Path(__file__).parent.parent.parent

LogPath = BaseDir.joinpath('logs')
LogPath.mkdir(parents=True, exist_ok=True)


class Config:
    DEBUG = True
    SECRET_KEY = '00cc52961e50dd04c2e7533f5a4c4e2b'
    LOG_LEVEL = 'DEBUG'

    # server  公网：121.36.24.44
    HOST = '192.168.0.102'
    DB_PORT = 3306
    REDIS_PORT = 6379

    # SQLAlchemy Config mysql.
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:123523@{HOST}:{DB_PORT}/myflask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TIMEZONE = 'Asia/Shanghai'

    # redis config
    REDIS_URL = f'redis://{HOST}:{REDIS_PORT}/0'
    REDIS_USERNAME = None
    REDIS_PASSWORD = None
    REDIS_DB = 0
    REDIS_DECODE_RESPONSES = True

    # static file.
    STATIC_FOLDER = BaseDir.joinpath('static')
    STATIC_URL_PATH = '/static'
    STATIC_FOLDER.mkdir(parents=True, exist_ok=True)

    # flask_jwt_extended
    JWT_SECRET_KEY = '710f9e2f0646d4a7df0d141c0717b4f1c8469e97d13a4b82875e19b1e3534202'
    JWT_ACCESS_TOKEN_EXPIRES = 7 * 24 * 60 * 60

    # ibs.amap.com key
    SWEET_KEY = '91025bcba94bb12189ac21d522b18b61'

    # mail server
    MAIL_ID = 'mhan_2010@163.com'
    MAIL_PWD = 'WTKOHBNHVZPCWYOB'
    MAIL_SMTP_SERVER = 'smtp.163.com'
    MAIL_SMTP_PORT = 25
