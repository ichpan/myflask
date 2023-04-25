#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from application.settings import Config


class DevConfig(Config):
    SQLALCHEMY_ECHO = True
