#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from application.settings import Config

broker_url = f'redis://{Config.HOST}'
result_backend = f'redis://{Config.HOST}:{Config.REDIS_PORT}/1'
task_serializer = 'json'
result_serializer = 'json'
result_expires = 60 * 60 * 24
accept_content = ['json', 'msgpack']
worker_concurrency = 10
