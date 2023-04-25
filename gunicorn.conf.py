#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing
from gevent import monkey

from application.settings import BaseDir

monkey.patch_all()

# port
bind = "0.0.0.0:5001"

workers = multiprocessing.cpu_count()
worker_class = 'gevent'

# Config log
loglevel = 'info'
accesslog = str(BaseDir.joinpath('logs/gunicorn.access.log'))
errorlog = str(BaseDir.joinpath('logs/gunicorn.error.log'))
