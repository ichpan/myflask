#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
redis_cli = FlaskRedis()
jwt = JWTManager()
bcrypt = Bcrypt()
cors = CORS()
csrf = CSRFProtect()
