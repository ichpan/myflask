#!/usr/bin/env python3
# -*-coding:utf-8 -*-

from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

app = Celery('proj', include=[
    'application.timed_task.tasks',
    'application.timed_task.weather',
])
app.config_from_object('application.settings.celeryconfig')

# 定时任务
# timedelta(seconds=5) 按秒执行依赖timedelta
app.conf.beat_schedule = {
    "time_teller": {
        "task": "application.timed_task.tasks.time_teller",
        "schedule": timedelta(hours=2)
    },
    "send_weather_info": {
        "task": "application.timed_task.weather.send_weather_info",
        "schedule": crontab(minute=0, hour=7)
    }
}
