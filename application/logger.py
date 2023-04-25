#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler


def setup_log(config):

    logging.basicConfig(level=config.LOG_LEVEL)

    fh = RotatingFileHandler("logs/app.log", maxBytes=1024 * 1024 * 300, backupCount=5)
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(filename)s] [%(funcName)s:%(lineno)d] %(message)s", "%Y-%m-%d %H:%M:%S"
    )
    fh.setFormatter(formatter)
    logging.getLogger().addHandler(fh)
