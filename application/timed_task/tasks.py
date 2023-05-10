#!/usr/bin/env python3
# -*-coding:utf-8 -*-

import time
from datetime import datetime

from application.timed_task.celery_app import app


@app.task
def time_teller():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return 'current_time is:{}'.format(current_time)


@app.task
def add(a, b):
    time.sleep(3)  # 模拟耗时
    return a + b
